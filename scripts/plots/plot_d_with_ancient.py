import os, sys
import matplotlib as mpl
from matplotlib import pyplot as plt
from argparse import ArgumentParser
import baltic.baltic as bt
import pandas as pd
import seaborn as sns
from datetime import timedelta, datetime
from matplotlib.lines import Line2D
from pymc3.stats import hpd
from collections import defaultdict, OrderedDict
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
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

    for k in tre.Objects:
        i = k.traits['location.set.prob'].index(max([float(t) for t in k.traits['location.set.prob']]))
        k.traits['location'] = k.traits['location.set'][i]

    travel_lineages = []
    for k in tre.Objects:
        try:
            if k.parent!=tre.root and k.traits['location']!=k.parent.traits['location']:
                travel_lineages.append(k)
        except:
            pass
    travel_lineages = sorted(travel_lineages, key=lambda x:x.absoluteTime)


    h = tre.treeHeight
    m = 2014
    print("Travel lineages:",len(travel_lineages))

    # xDates=[n for n in range(1,math.ceil(tre.root.traits['height'])+1)] ## create timeline
    xDates=[n for n in range(math.floor(tre.root.absoluteTime),2015)] ## create timeline


    # heights=[k.traits['height'] for k in travel_lineages] ## get absolute times of each branch in the tree
    heights=[k.absoluteTime for k in travel_lineages]
    print(sorted(heights))
    height_normalization=create_normalization([-2000,2015],0.0,1.0) ## create a normalization based on timeline, where earliest day is 0.0 and latest is 1.0

    cmap=mpl.cm.get_cmap('cividis_r') ## colour map

    # nested dictionary counting transitions from one loc to another
    # i.e. transition_counts[from_location][to_another] => 3
    transition_counts = { "Africa" : {},
                          "Americas" : {},
                          "EastSouthAsia" : {},
                          "Europe" : {},
                          "WestCentralAsia" : {} }
    for k in travel_lineages: ## iterate through lineages which have switched location
        locA=k.traits['location'] ## get location of current lineage
        locB=k.parent.traits['location'] ## get location of where it came from

        # add to transition count
        if locA in transition_counts[locB].keys():
            transition_counts[locB][locA] += 2
        else:
            transition_counts[locB][locA] = 0

        # oriX,oriY=region_coords[locA] ## get population centroid coordinates
        # desX,desY=region_coords[locB]
        desX,desY=region_coords[locA] ## get population centroid coordinates
        oriX,oriY=region_coords[locB]


        # normalized_height=height_normalization(k.traits['height']) ## normalize heights of lineages
        # normalized_parent_height=height_normalization(k.parent.traits['height'])
        normalized_height=height_normalization(k.absoluteTime) ## normalize heights of lineages
        normalized_parent_height=height_normalization(k.parent.absoluteTime)


        distance=math.sqrt(math.pow(oriX-desX,2)+math.pow(oriY-desY,2)) ## find travelling distance

        adjust_d=-1*(distance*(1+transition_counts[locB][locA]/5)/5) ## position Bezier curve control point according to an arbitrary function

        n=Bezier_control((oriX,oriY),(desX,desY),adjust_d) ## control point perpendicular to midway between point A and B at a distance adjust_d

        curve=Bezier([(oriX,oriY),n,(desX,desY)],0.0,1.0,num=30) ## get Bezier line coordinates

        zorder_func=lambda k: (50000-math.ceil(k.parent.height))
        print(zorder_func(k))

        for i in range(len(curve)-1): ## iterate through Bezier curve coordinates, alter colour according to height
            x1,y1=curve[i]
            x2,y2=curve[i+1]
            frac=i/float(len(curve)) ## fraction along line

            ax.plot([x1,x2],[y1,y2],
                    lw=1+4*(1-frac),
                    color=cmap(normalized_parent_height-(normalized_height-normalized_parent_height)*(1-frac)),
                    zorder=zorder_func(k)) ## curve tapers and changes colour

    #################################
    ## Background map from GEOJson ##
    #################################
    country_region_df = pd.read_csv('metadata/country_region_partial.tsv',sep='\t')
    country_region = { row['country']: row['continent'] for index, row in country_region_df.iterrows() }
    colors['antarctica'] = 'lightgrey'
    for i,loc in enumerate(locations): ## iterate over locations
        region=country_region[loc] ## get country

        regionColor=colors[region.lower()] ## get colour map

        ax.add_collection(PatchCollection(polygons[loc],facecolor=regionColor,edgecolor='black',lw=1,zorder=-1)) ## polygon colour pale

        lon,lat=region_coords[region] ## population centroid coordinates

        size=[k.traits['location'] for k in tre.Objects].count(loc) ## circle size proportional to branches in location
        size=50+size
        ax.scatter(lon,lat,size,facecolor=desaturate(regionColor,1.0),edgecolor='k',lw=2,zorder=200000) ## plot circle, edge coloured inversely from main colour

    ax.set_ylim(-60,90)
    ax.set_axis_off()

    colorbarTextSize=15 ## add colourbars
    colorbarTickLabelSize=12
    colorbarWidth=0.02
    colorbarHeight=0.2

    ax2 = ax.get_figure().add_axes([0.40, 0.155, colorbarHeight, colorbarWidth]) ## add dummy axes

    mpl.colorbar.ColorbarBase(ax2, cmap=mpl.cm.get_cmap('cividis_r'),norm=mpl.colors.Normalize(-2000,2015),orientation='horizontal')
    ax2.xaxis.set_major_locator(mpl.ticker.LinearLocator(numticks=9)) ## add colour bar to axes

    xaxis_labels=[ '-2000', '-1500', '-1000', '-500', '0', '500', '1000', '1500', '2014' ]

    ax2.set_xticklabels(xaxis_labels) ## set colour bar tick labels
    ax2.xaxis.set_label_position('top') ## colour bar label at the top
    ax2.set_xlabel('Transition Time',color='k',size=colorbarTextSize) ## colour bar label is "date"
    ax2.tick_params(labelcolor='k',size=10,labelsize=colorbarTickLabelSize,labelrotation=45) ## adjust axis parameters
    print("Transition counts:")
    print(transition_counts)

def add_legend(color_dict, ax):
    legend_elements = []
    names = []
    for name,clr in color_dict.items():
        dot = Line2D([0], [0], marker='o', color='w', label=name,
                          markerfacecolor=clr, markersize=15)
        names.append(name)
        legend_elements.append(dot)
    name_fix = lambda x: x.replace('europe','Europe').replace('westcentralasia','West/Central Asia').replace('eastsouthasia','East/South Asia').replace('americas','Americas').replace('africa','Africa')
    labels = [ name_fix(name) for name in names]
    ax.ticklabel_format(useOffset=False, style='plain')
    ax.legend(handles=legend_elements, labels=labels, loc='lower left', fontsize=12,frameon=False)
    ax.set_axis_off()

def plot_BEAST(tre,gjs,log,o_file):
    # set color color_palette
    # country_color = set_country_colors(tre)
    # add tree plot
    # fig, ax = plt.subplots(figsize=(15,15))
    r = 8
    fig, ax3 =  plt.subplots(figsize=(15,15), dpi=600)
    # set x axis to be time
    x_attr=lambda k: k.absoluteTime

    fc = ((.99,.99,.99))
    ax3.set_facecolor(fc)
    x_lim = (-2000,2025)

    cmap = { 'europe' : 'indianred',
             'eastsouthasia' : 'steelblue',
             'westcentralasia' : 'mediumpurple',
             'americas' : 'goldenrod',
             'africa' : 'yellowgreen' }


    c_func = lambda k: cmap[k.traits['location.set'][k.traits['location.set.prob'].index(max([float(t) for t in k.traits['location.set.prob']]))].lower()]
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
    tre.plotPoints(ax=ax3,
                   x_attr=x_attr,
                   colour_function=lambda x: 'k', # tip shape outline
                   size_function=p_o_func)
    tre.plotPoints(ax=ax3,
                   x_attr=x_attr,
                   colour_function=c_func,
                   size_function=p_i_func)

    ax3.get_yaxis().set_ticks([])
    ax3.xaxis.tick_top()
    ax3.set_ylim(-125,775)

    lax = plt.axes([.13,.5,.05,.05])
    add_legend(cmap,lax)
    map_location = (.1,.14) # location of map inset within larger figure
    map_ar = (.62,.3) # aspect ratio of map inset
    map_scale = 1.05 # scale of map inset
    inside = plt.axes([map_location[0], map_location[1], map_ar[0]*map_scale, map_ar[1]*map_scale])
    add_static_map(tre,gjs,cmap,inside)

    fig.suptitle( f"HBV-D Phylogeography",fontsize=20 )

    # export to pdf
    plt.savefig(o_file,format='pdf')

    # export to png
    plt.savefig(o_file.replace('.pdf','.png'), format='png')

if __name__ == '__main__':

    folder = "phylogeography/d"
    filestem = "HBV-D_phylogeography"
    log = "beast_files/d/combined/HBV-D_combined.log"
    output = "HBV-D_phylogeography_and_mcc_tree"
    burnin = 0
    geojson = "metadata/world.geo.json"

    trees_file = f"{folder}/{filestem}.trees"
    log_file = log
    # plot tree
    mcc_tree = bt.loadNexus(f"{folder}/{filestem}.mcc.tre",variableDate=True,tip_regex='\/([\-0-9]+)',date_fmt='%Y',)
    print("Root time:")
    print(mcc_tree.root.absoluteTime)
    log = pd.read_csv(log_file,sep='\t',skiprows=0,index_col=0)
    log = log.loc[burnin:].copy()
    plot_file = f"{folder}/{output}.pdf"
    plot_BEAST(mcc_tree,geojson,log,plot_file)
