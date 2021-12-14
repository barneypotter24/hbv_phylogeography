import os, sys
import matplotlib as mpl
from matplotlib import pyplot as plt
from argparse import ArgumentParser
import baltic.baltic as bt
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
# import cartopy.crs as ccrs
from utils import *
import math

def determine_location(k):
    if 'location' in k.traits.keys():
        location = k.traits['location']

    elif ('location.set' in k.traits.keys()) and ('location.set.prob' in k.traits.keys()):
        s = k.traits['location.set']
        sp = k.traits['location.set.prob']
        location = s[sp.index(max(sp))]

    return location

def plot_tmrca_kde(log,ax):
    sns.kdeplot(log['age(root)'],shade=True,color='grey',legend=False,ax=ax)
    ax.get_yaxis().set_ticks([])
    yl = max(ax.get_ylim())
    ax.set_ylim(0,yl+50)
    ax.get_yaxis().set_ticks([])

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

def clock_rate_plot(log,ax):
    sns.boxenplot(log['meanRate'],orient="vertical",color='steelblue',ax=ax)
    ax.axes.set_ylabel("rate (substitutions/site/year)",fontsize=12)
    ax.set_title('Evolutionary rate',fontsize=12)

def add_tmrca_text(log,ax):
    mean_tmrca = convert_partial_year(log['age(root)'].mean())
    tmrca_hpd = [convert_partial_year(x) for x in hpd(log['age(root)'].values,0.95)]
    mean_clock = '%.2E' %log['meanRate'].mean()
    clock_hpd = ['%.2E' %x for x in hpd(log['meanRate'].values,0.95)]
    ax.text(ax.get_xlim()[0]+0.02,ax.get_ylim()[1]*0.6 ,
             f"TMRCA: {(mean_tmrca)}\n\nHPD95%: {tmrca_hpd[0]} to {tmrca_hpd[1]}",fontsize=15)
    ax.text(ax.get_xlim()[0]+0.02,ax.get_ylim()[1]*0.5 ,
             f"Clock rate: {mean_clock}\n\nHPD95%: {clock_hpd[0]} to {clock_hpd[1]}",fontsize=15)

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

    transition_color = "Reds"

    travel_lineages = []
    for k in tre.Objects:
        try:
            if k.parent!=tre.root and determine_location(k)!=determine_location(k.parent):
                travel_lineages.append(k)
        except:
            pass
    travel_lineages = sorted(travel_lineages, key=lambda x:x.absoluteTime)

    # print all the travel lineage times
    h = tre.treeHeight
    m = 2014
    print("Travel lineages:")
    for lineage in travel_lineages:
        print(f"({lineage.parent.absoluteTime},{lineage.absoluteTime})")

    # travel_lineages=sorted([k for k in tre.Objects if k.parent!=tre.root and k.traits[traitName]!=k.parent.traits[traitName]],key=lambda x:x.absoluteTime) ## only interested in lineages travelling

    xDates=[n for n in range(1,math.ceil(tre.root.traits['height'])+1)] ## create timeline
    heights=[k.absoluteTime for k in travel_lineages] ## get absolute times of each branch in the tree
    height_normalization=create_normalization([-2500,2014],0.0,1.0) ## create a normalization based on timeline, where earliest day is 0.0 and latest is 1.0

    cmap=mpl.cm.get_cmap(transition_color) ## colour map

    # nested dictionary counting transitions from one loc to another
    # i.e. transition_counts[from_location][to_another] => 3
    transition_counts = { "Africa" : {},
                          "Americas" : {},
                          "EastSouthAsia" : {},
                          "Europe" : {},
                          "WestCentralAsia" : {} }
    for k in travel_lineages: ## iterate through lineages which have switched location
        locA=determine_location(k) ## get location of current lineage
        locB=determine_location(k.parent) ## get location of where it came from

        # add to transition count
        if locA in transition_counts[locB].keys():
            transition_counts[locB][locA] += 1
        else:
            transition_counts[locB][locA] = 0

        # oriX,oriY=region_coords[locA] ## get population centroid coordinates
        # desX,desY=region_coords[locB]
        desX,desY=region_coords[locA] ## get population centroid coordinates
        oriX,oriY=region_coords[locB]

        normalized_height=height_normalization(k.absoluteTime) ## normalize heights of lineages
        normalized_parent_height=height_normalization(k.parent.absoluteTime)

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
    country_region_df = pd.read_csv('metadata/country_region_partial.tsv',sep='\t')
    country_region = { row['country']: row['continent'] for index, row in country_region_df.iterrows() }
    colors['antarctica'] = 'lightgrey'
    for i,loc in enumerate(locations): ## iterate over locations
        region=country_region[loc] ## get country

        regionColor=colors[region.lower()] ## get colour map

        ax.add_collection(PatchCollection(polygons[loc],facecolor=regionColor,edgecolor='black',lw=1,zorder=-1)) ## polygon colour pale

        lon,lat=region_coords[region] ## population centroid coordinates

        size=[determine_location(k) for k in tre.Objects].count(loc) ## circle size proportional to branches in location
        size=50+size
        ax.scatter(lon,lat,size,facecolor=desaturate(regionColor,1.0),edgecolor='k',lw=2,zorder=200000) ## plot circle, edge coloured inversely from main colour

    ax.set_ylim(-60,90)
    ax.set_axis_off()

    colorbarTextSize=20 ## add colourbars
    colorbarTickLabelSize=18
    colorbarWidth=0.02
    colorbarHeight=0.2

    ax2 = ax.get_figure().add_axes([0.38, 0.18, colorbarHeight, colorbarWidth]) ## add dummy axes

    mpl.colorbar.ColorbarBase(ax2, cmap=mpl.cm.get_cmap(transition_color),norm=mpl.colors.Normalize(-2500,2014.),orientation='horizontal')
    ax2.xaxis.set_major_locator(mpl.ticker.LinearLocator(numticks=10)) ## add colour bar to axes

    xaxis_labels=[ '-2500', '-2000', '-1500', '-1000', '-500', '0', '500', '1000', '1500', '2014' ]

    ax2.set_xticklabels(xaxis_labels) ## set colour bar tick labels
    ax2.xaxis.set_label_position('top') ## colour bar label at the top
    ax2.set_xlabel('Transition Time',color='k',size=colorbarTextSize) ## colour bar label is "date"
    ax2.tick_params(labelcolor='k',size=18,labelsize=colorbarTickLabelSize,labelrotation=45) ## adjust axis parameters

    print("Transition counts:")
    print(transition_counts)

def add_legend(color_dict, ax):
    legend_elements = []
    for name,clr in color_dict.items():
        dot = Line2D([0], [0], marker='o', color='w', label=name,
                          markerfacecolor=clr, markersize=15)
        legend_elements.append(dot)
    labels = [ "Europe", "East/South Asia", "West/Central Asia", "Americas", "Africa"]
    ax.ticklabel_format(useOffset=False, style='plain')
    ax.legend(handles=legend_elements, labels=labels, loc='lower left', fontsize=18,frameon=False)
    ax.set_axis_off()

def plot_BEAST(tre,gjs,log,o_file):
    # set color color_palette
    # country_color = set_country_colors(tre)
    # add tree plot
    # fig, ax = plt.subplots(figsize=(15,15))
    r = 8
    fig, (ax0, ax1, ax2, ax3) =  plt.subplots(1, 4,
                                              figsize=(21,15),
                                              gridspec_kw={'width_ratios': [1, 1, 1, r]},
                                              dpi=300)

    fc = (.99,.99,.99)
    ax0.set_facecolor(fc)
    ax1.set_facecolor(fc)
    ax2.set_facecolor(fc)
    ax3.set_facecolor(fc)
    # set x axis to be time
    x_attr=lambda k: k.absoluteTime


    x_lims = [ (-2650,-2050),
               (-825,-550),
               (-250,550),
               (1775,2025)]

    cmap = { 'europe' : 'indianred',
             'eastsouthasia' : 'steelblue',
             'westcentralasia' : 'mediumpurple',
             'americas' : 'goldenrod',
             'africa' : 'yellowgreen' }

    c_func = lambda k: cmap[determine_location(k).lower()]
    p_o_func = lambda x: 14
    p_i_func = lambda x: 9
    w_func = lambda x: 1.

    #####################
    #### first  plot ####
    #####################
    tre.plotTree(ax=ax0,x_attr=x_attr,colour_function=c_func,
                   branchWidth=w_func)
    mrsd = max([x.absoluteTime for x in tre.getExternal()])
    ax0.set_xlim(x_lims[0][0],x_lims[0][1])
    # color tips by country
    tre.plotPoints(ax=ax0,x_attr=x_attr,colour_function=lambda x: 'k', # tip shape outline
                   size_function=p_o_func)
    tre.plotPoints(ax=ax0,x_attr=x_attr,colour_function=c_func,
                   size_function=p_i_func,)

    ######################
    #### second  plot ####
    ######################
    tre.plotTree(ax=ax1,x_attr=x_attr,colour_function=c_func,
                    branchWidth=w_func)
    mrsd = max([x.absoluteTime for x in tre.getExternal()])
    ax1.set_xlim(x_lims[1][0],x_lims[1][1])
    # color tips by country
    tre.plotPoints(ax=ax1,x_attr=x_attr,colour_function=lambda x: 'k', # tip shape outline
                   size_function=p_o_func)
    tre.plotPoints(ax=ax1,x_attr=x_attr,colour_function=c_func,
                   size_function=p_i_func,)

    #####################
    #### third  plot ####
    #####################
    tre.plotTree(ax=ax2,x_attr=x_attr,colour_function=c_func,
                    branchWidth=w_func)
    mrsd = max([x.absoluteTime for x in tre.getExternal()])
    ax2.set_xlim(x_lims[2][0],x_lims[2][1])
    # color tips by country
    tre.plotPoints(ax=ax2,x_attr=x_attr,colour_function=lambda x: 'k', # tip shape outline
                   size_function=p_o_func)
    tre.plotPoints(ax=ax2,x_attr=x_attr,colour_function=c_func,
                   size_function=p_i_func,)

    ######################
    #### fourth  plot ####
    ######################
    tre.plotTree(ax=ax3,x_attr=x_attr,colour_function=c_func,
                    branchWidth=w_func)
    mrsd = max([x.absoluteTime for x in tre.getExternal()])
    ax3.set_xlim(x_lims[3][0],x_lims[3][1])
    # color tips by country
    tre.plotPoints(ax=ax3,x_attr=x_attr,colour_function=lambda x: 'k', # tip shape outline
                   size_function=p_o_func)
    tre.plotPoints(ax=ax3,x_attr=x_attr,colour_function=c_func,
                   size_function=p_i_func,)

    # remove labels between axes
    ax0.spines['right'].set_visible(False)
    ax1.spines['left'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax3.spines['left'].set_visible(False)

    ax0.yaxis.tick_left()
    ax0.tick_params(labelleft=False,
                    axis="y",
                    width=0,
                    length=0)  # put tick labels at the left
    ax1.tick_params(labelleft=False,
                    axis="y",
                    width=0,
                    length=0)  # don't put tick labels at the left
    ax2.tick_params(labelleft=False,
                    axis="y",
                    width=0,
                    length=0)  # don't put tick labels at the left
    ax3.tick_params(labelleft=False,
                    axis="y",
                    width=0,
                    length=0)  # don't put tick labels at the left

    ax0.tick_params(axis="x",labelsize=18,labelrotation=45)
    ax1.tick_params(axis="x",labelsize=18,labelrotation=45)
    ax2.tick_params(axis="x",labelsize=18,labelrotation=45)
    ax3.tick_params(axis="x",labelsize=18,labelrotation=45)
    ax0.xaxis.tick_top()
    ax1.xaxis.tick_top()
    ax2.xaxis.tick_top()
    ax3.xaxis.tick_top()

    # Add diagonal breaks to the axes
    d = .005  # how big to make the diagonal lines in axes coordinates
    # arguments to pass to plot, just so we don't keep repeating them
    kwargs = dict(transform=ax0.transAxes, color='k', clip_on=False)

    # first plot
    ax0.plot((1 - r*d, 1 + r*d), (1 - d, 1 + d), **kwargs) # top-right
    ax0.plot((1 - r*d, 1 + r*d), (0 - d, 0 + d), **kwargs)  # bottom-right

    # second plot
    kwargs.update(transform=ax1.transAxes)  # switch to the bottom axes
    ax1.plot((1 - r*d, 1 + r*d), (1 - d, 1 + d), **kwargs) # top-right
    ax1.plot((1 - r*d, 1 + r*d), (0 - d, 0 + d), **kwargs)  # bottom-right
    ax1.plot((0 - r*d, 0 + r*d), (1 - d, 1 + d), **kwargs) # top-left
    ax1.plot((0 - r*d, 0 + r*d), (0 - d, 0 + d), **kwargs)  # bottom-left

    # third plot
    kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
    ax2.plot((1 - r*d, 1 + r*d), (1 - d, 1 + d), **kwargs) # top-right
    ax2.plot((1 - r*d, 1 + r*d), (0 - d, 0 + d), **kwargs)  # bottom-right
    ax2.plot((0 - r*d, 0 + r*d), (1 - d, 1 + d), **kwargs) # top-left
    ax2.plot((0 - r*d, 0 + r*d), (0 - d, 0 + d), **kwargs)  # bottom-left

    # fourth plot
    kwargs.update(transform=ax3.transAxes)  # switch to the bottom axes
    ax3.plot((0 - d, 0 + d), (1 - d, 1 + d), **kwargs) # top-left
    ax3.plot((0 - d, 0 + d), (0 - d, 0 + d), **kwargs)  # bottom-left


    # add indicator for posterior support
    # text_func=lambda k: "⁎" if k.traits['posterior']>0.5 else ""
    # text_pos_func=lambda k: (k.absoluteTime,k.y+0.2)
    # target_func=lambda k: k.branchType=='node' ## only target nodes
    # tre.addText(ax,position=text_pos_func,target=target_func,text=text_func,size=15,color='black',weight='bold')
    # ax.annotate('⁎ indicates nodes with posterior>0.5  ', xy=(1, 0), xycoords='axes fraction', fontsize=12,
    #             horizontalalignment='right', verticalalignment='bottom')
    # plot aligned tip labels
    # plot_tip_labels(tre,ax)
    # plot legend
    # plot tmrca kde on twin x axis
    # ax2 = ax.twinx()
    # plot_tmrca_kde(log,ax2)
    #plot clock rate boxplot
    lax = plt.axes([.13,.5,.05,.05])
    add_legend(cmap,lax)
    map_location = (.13,.16) # location of map inset within larger figure
    map_ar = ((5/7)*.62,.3) # aspect ratio of map inset
    map_scale = 1.25 # scale of map inset
    inside = plt.axes([map_location[0], map_location[1], map_ar[0]*map_scale, map_ar[1]*map_scale])
    add_static_map(tre,gjs,cmap,inside)
    #plot time to ancestors boxplot
    # inside2 = plt.axes([.35, .65, .1, .2])
    # time_delta_plot(tre,inside2)
    # add tmrca dates text
    # add_tmrca_text(log,ax2)
    # add title
    # fig.suptitle( f"HBV-A Phylogeography",fontsize=20 )

    # export to pdf
    plt.savefig(o_file,format='pdf')

    # export to png
    plt.savefig(o_file.replace('.pdf', '.png'), format='png')

if __name__ == '__main__':

    folder = "phylogeography/a"
    log = "beast_files/a/combined/HBV-A_combined.log"
    filestem = "HBV-A_phylogeography"
    output = "HBV-A_phylogeography_and_mcc_tree"
    burnin = 0
    geojson = "metadata/world.geo.json"

    trees_file = f"{folder}/{filestem}.trees"
    log_file = log
    # plot tree
    mcc_tree = bt.loadNexus(f"{folder}/{filestem}.mcc.tre",variableDate=True,tip_regex='\/([\-0-9]+)',date_fmt='%Y',)
    print("Root height:")
    print(mcc_tree.treeHeight)
    log = pd.read_csv(log_file,sep='\t',skiprows=0,index_col=0)
    log = log.loc[burnin:].copy()
    plot_file = f"{folder}/{output}.pdf"
    plot_BEAST(mcc_tree,geojson,log,plot_file)
