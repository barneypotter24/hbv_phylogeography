import os, sys
import matplotlib as mpl
from matplotlib import pyplot as plt
from argparse import ArgumentParser
import baltic as bt
import pandas as pd
import seaborn as sns
from datetime import timedelta, datetime
from matplotlib.lines import Line2D
from Bio import SeqIO
from pymc3.stats import hpd
import subprocess
from collections import defaultdict, OrderedDict
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import cartopy.crs as ccrs
from utils import *
import math

def convert_partial_year(number):
    year = int(number)
    d = timedelta(days=(number - year)*(365 + is_leap(year)))
    if year > 0:
        day_one = datetime(year,1,1)
        date = d + day_one
        return date.date().isoformat()
    else:
        day_one = datetime(-year,1,1)
        date = d + day_one
        return '-' +date.date().isoformat()

def is_leap(x):
    if int(x) % 4 == 0:
        return True
    else:
        return False

def set_country_colors(tre):
    tips = tre.getExternal()
    continent_country = defaultdict(list)
    for x in tips:
        continent_country[x.name.split("|")[-3]].append(x.name.split("|")[-2])
    num_continents = len(set(continent_country.keys()))
    # continent_pal =  sns.color_palette("Accent",n_colors=num_continents)
    # hacky way
    continent_pal = {'Asia':'Blues', 'NorthAmerica':'Reds', 'Europe':'Greens', 'Oceania':'copper'}
    country_color_dict = OrderedDict()
    for cont,countries in continent_country.items():
        country_clrs = sns.color_palette(continent_pal[cont], len(countries))
        for i,c in enumerate(countries):
            country_color_dict[c] = country_clrs[i]
    return country_color_dict

def findTimeDelta(date1,date2):
    """Returns number of days separating two decimal dates
    """
    delta = date2-date1
    years = int(delta)
    days = (delta - years)*365
    return (365*years+days)

def plot_tip_labels(tre,ax):
    tips = tips = tre.getExternal()
    text_func_tips=lambda k: ''#k.name.split("|")[1]
    mrsd = max([x.absoluteTime for x in tips])
    tip_label_pos = mrsd+0.1
    text_pos_func = lambda k: (tip_label_pos,k.y+0.1)
    target_func_tips=lambda k: k.branchType=='leaf'
    tre.addText(ax,position=text_pos_func,target=target_func_tips,text=text_func_tips,size=10,color='black')
    # plot dash to labels
    for tip in tips:
        x = [tip.absoluteTime,tip_label_pos]
        y= [tip.y,tip.y]
        ax.plot(x,y,linestyle=':',color='grey')

def time_delta_plot(tre,ax):
    tips = tre.getExternal()
    time_to_ancestor_tips = {}
    for t in tips:
        time_to_ancestor_tips[t.name] = findTimeDelta(t.parent.absoluteTime,t.absoluteTime)
    time_deltas = (pd.DataFrame(time_to_ancestor_tips,index=['days']).T)
    sns.boxenplot(time_deltas['days'],orient='v',ax=ax,color='darksalmon')
    #sns.swarmplot(time_deltas['days'],color='silver',orient='v',
    #                   edgecolor='w',linewidth=0.3,alpha=0.9,size=7,ax=ax)
    ax.set_title("Time from taxa to ancestor")
    ax.set_ylabel("time (days)",fontsize=12)
    ax.set_ylim([-1,time_deltas['days'].max()+1])
    ax.set_yscale("log")

def add_static_map(tre, gjs, colors, ax):
    '''
    This is taken from Gytis' ebov static map
    '''
    # Define the lon,lat values of each regional pseudo-centroid
    region_coords = { "Africa" :	(16.430973, 13.373588),
                      "Americas" :	(-86.506117, 13.031318),
                      "EastSouthAsia" :	(105.310561, 31.770208),
                      "Europe" :	(14.323098, 49.012654),
                      "WestCentralAsia" :	(59., 40.0),
                      "Antarctica" : (0.00001, -89.99999) }

    # load geojson to define polygons and locations for the map
    polygons, locations = load_geojson_to_polygons(gjs)

    # use ccrs coastlines
    traitName='Region' ## name of locations trait in tree

    travel_lineages = []
    for k in tre.Objects:
        try:
            if k.parent!=tre.root and k.traits[traitName]!=k.parent.traits[traitName]:
                travel_lineages.append(k)
        except:
            pass
    travel_lineages = sorted(travel_lineages, key=lambda x:x.absoluteTime)

    h = tre.treeHeight
    m = 2014
    print("Travel lineages:")
    for lineage in travel_lineages:
        print(f"({lineage.parent.absoluteTime},{lineage.absoluteTime})")

    # travel_lineages=sorted([k for k in tre.Objects if k.parent!=tre.root and k.traits[traitName]!=k.parent.traits[traitName]],key=lambda x:x.absoluteTime) ## only interested in lineages travelling

    xDates=[n for n in range(1,math.ceil(tre.root.traits['height'])+1)] ## create timeline

    heights=[k.traits['height'] for k in travel_lineages] ## get absolute times of each branch in the tree
    height_normalization=create_log_normalization([xDates[0],xDates[-1]],0.0,1.0) ## create a normalization based on timeline, where earliest day is 0.0 and latest is 1.0

    cmap=mpl.cm.get_cmap('cividis') ## colour map

    # nested dictionary counting transitions from one loc to another
    # i.e. transition_counts[from_location][to_another] => 3
    transition_counts = { "Africa" : {},
                          "Americas" : {},
                          "EastSouthAsia" : {},
                          "Europe" : {},
                          "WestCentralAsia" : {} }
    for k in travel_lineages: ## iterate through lineages which have switched location
        locA=k.traits[traitName] ## get location of current lineage
        locB=k.parent.traits[traitName] ## get location of where it came from

        # add to transition count
        if locA in transition_counts[locB].keys():
            transition_counts[locB][locA] += 1
        else:
            transition_counts[locB][locA] = 0

        # oriX,oriY=region_coords[locA] ## get population centroid coordinates
        # desX,desY=region_coords[locB]
        desX,desY=region_coords[locA] ## get population centroid coordinates
        oriX,oriY=region_coords[locB]

        normalized_height=height_normalization(k.traits['height']) ## normalize heights of lineages
        normalized_parent_height=height_normalization(k.parent.traits['height'])

        distance=math.sqrt(math.pow(oriX-desX,2)+math.pow(oriY-desY,2)) ## find travelling distance

        adjust_d=-1*(distance*(1+transition_counts[locB][locA]/5)/5) ## position Bezier curve control point according to an arbitrary function

        n=Bezier_control((oriX,oriY),(desX,desY),adjust_d) ## control point perpendicular to midway between point A and B at a distance adjust_d

        curve=Bezier([(oriX,oriY),n,(desX,desY)],0.0,1.0,num=30) ## get Bezier line coordinates

        for i in range(len(curve)-1): ## iterate through Bezier curve coordinates, alter colour according to height
            x1,y1=curve[i]
            x2,y2=curve[i+1]
            frac=i/float(len(curve)) ## fraction along line

            ax.plot([x1,x2],[y1,y2],lw=1+4*(1-frac),color=cmap(normalized_parent_height+(normalized_height-normalized_parent_height)*(1-frac)),zorder=int(normalized_height*10000)) ## curve tapers and changes colour

    #################################
    ## Background map from GEOJson ##
    #################################
    country_region_df = pd.read_csv('../../phylogeography/assets/country_region_partial.tsv',sep='\t')
    country_region = { row['country']: row['continent'] for index, row in country_region_df.iterrows() }
    colors['antarctica'] = 'lightgrey'
    for i,loc in enumerate(locations): ## iterate over locations
        region=country_region[loc] ## get country

        regionColor=colors[region.lower()] ## get colour map

        ax.add_collection(PatchCollection(polygons[loc],facecolor=regionColor,edgecolor='black',lw=1,zorder=-1)) ## polygon colour pale

        lon,lat=region_coords[region] ## population centroid coordinates

        size=[k.traits[traitName] for k in tre.Objects].count(loc) ## circle size proportional to branches in location
        size=50+size
        ax.scatter(lon,lat,size,facecolor=desaturate(regionColor,1.0),edgecolor='k',lw=2,zorder=200000) ## plot circle, edge coloured inversely from main colour

    ax.set_ylim(-60,90)
    ax.set_axis_off()

    colorbarTextSize=15 ## add colourbars
    colorbarTickLabelSize=12
    colorbarWidth=0.02
    colorbarHeight=0.2

    ax2 = ax.get_figure().add_axes([0.40, 0.155, colorbarHeight, colorbarWidth]) ## add dummy axes

    mpl.colorbar.ColorbarBase(ax2, cmap=mpl.cm.get_cmap('cividis_r'),norm=mpl.colors.Normalize(xDates[0],xDates[-1]),orientation='horizontal')
    ax2.xaxis.set_major_locator(mpl.ticker.LinearLocator(numticks=10)) ## add colour bar to axes

    xaxis_labels=[ '1800', '1825', '1850', '1875', '1900', '1925', '1950', '1975', '2000', '2025']

    ax2.set_xticklabels(xaxis_labels) ## set colour bar tick labels
    ax2.xaxis.set_label_position('top') ## colour bar label at the top
    ax2.set_xlabel('Transition Time',color='k',size=colorbarTextSize) ## colour bar label is "date"
    ax2.tick_params(labelcolor='k',size=10,labelsize=colorbarTickLabelSize,labelrotation=45) ## adjust axis parameters
    print("Transition counts:")
    print(transition_counts)

def add_legend(color_dict, ax):
    legend_elements = []
    for name,clr in color_dict.items():
        dot = Line2D([0], [0], marker='o', color='w', label=name,
                          markerfacecolor=clr, markersize=15)
        legend_elements.append(dot)
    labels = [ "Africa", "Americas", "East/South Asia", "Europe", "West/Central Asia"]
    ax.ticklabel_format(useOffset=False, style='plain')
    ax.legend(handles=legend_elements, labels=labels, loc='lower left', fontsize=12,frameon=False)
    ax.set_axis_off()

def plot_BEAST(tre,gjs,o_file):
    # set color color_palette
    # country_color = set_country_colors(tre)
    # add tree plot
    # fig, ax = plt.subplots(figsize=(15,15))
    r = 8
    fig, ax3 =  plt.subplots(figsize=(15,15))
    # set x axis to be time
    x_attr=lambda k: k.absoluteTime

    fc = ((.99,.99,.99))
    ax3.set_facecolor(fc)
    x_lim = (1800,2015)

    cmap = { 'europe' : 'indianred',
             'eastsouthasia' : 'steelblue',
             'westcentralasia' : 'mediumpurple',
             'americas' : 'goldenrod',
             'africa' : 'yellowgreen' }

    c_func = lambda k: cmap[k.traits['Region'].lower()]
    p_o_func = lambda x: 14
    p_i_func = lambda x: 9
    w_func = lambda x: 1.

    ######################
    ##### tree  plot #####
    ######################
    tre.plotTree(ax=ax3,x_attr=x_attr,colour_function=c_func,
                    branchWidth=w_func)
    mrsd = max([x.absoluteTime for x in tre.getExternal()])
    ax3.set_xlim(x_lim[0],x_lim[1])
    # color tips by country
    tre.plotPoints(ax=ax3,x_attr=x_attr,colour_function=lambda x: 'k', # tip shape outline
                   size_function=p_o_func)
    tre.plotPoints(ax=ax3,x_attr=x_attr,colour_function=c_func,
                   size_function=p_i_func,)

    ax3.get_yaxis().set_ticks([])
    ax3.xaxis.tick_top()
    ax3.set_ylim(-135,235)

    lax = plt.axes([.13,.5,.05,.05])
    add_legend(cmap,lax)
    map_location = (.1,.14) # location of map inset within larger figure
    map_ar = (.62,.3) # aspect ratio of map inset
    map_scale = 1.05 # scale of map inset
    inside = plt.axes([map_location[0], map_location[1], map_ar[0]*map_scale, map_ar[1]*map_scale])
    add_static_map(tre,gjs,cmap,inside)

    epi_day = o_file.split('/')[-1].replace('arambaut.','').replace('.pdf','')
    fig.suptitle( f"HBV-E Phylogeography",fontsize=20 )

    # export to pdf
    plt.savefig(o_file,format='pdf')

    # export to png
    plt.savefig(o_file.replace('.pdf','.png'), format='png')

if __name__ == '__main__':
    folder = "../../phylogeography/e_modern"
    filestem = "HBV-E_phylogeography"
    output = "HBV-E_phylogeography_and_mcc_tree"
    burnin = 0
    geojson = "../../phylogeography/assets/world.geo.json"

    trees_file = f"{folder}/{filestem}.trees"
    # plot tree
    mcc_tree = bt.loadNexus(f"{folder}/{filestem}.mcc.tre",variableDate=True,tip_regex='\/([\-0-9]+)',date_fmt='%Y',)
    print("Root time:")
    print(mcc_tree.root.absoluteTime)
    plot_file = f"{folder}/{output}.pdf"
    plot_BEAST(mcc_tree,geojson,plot_file)
