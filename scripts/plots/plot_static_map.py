'''plot_static_map.py'''
import os, sys
import matplotlib as mpl
from matplotlib import pyplot as plt
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
from matplotlib import collections  as mc


def add_static_map(gjs, colors, ax):

    # Define the lon,lat values of each regional pseudo-centroid
    region_coords = { "Africa" :	(16.430973, 13.373588),
                      "Americas" :	(-86.506117, 13.031318),
                      "EastSouthAsia" :	(105.310561, 31.770208),
                      "Europe" :	(14.323098, 49.012654),
                      "WestCentralAsia" :	(59., 40.0),
                      "Antarctica" : (0.00001, -89.99999) }

    # load geojson to define polygons and locations for the map
    polygons, locations = load_geojson_to_polygons(gjs)
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

        size=1 ## circle size proportional to branches in location
        size=50+size
        ax.scatter(lon,lat,size,facecolor=desaturate(regionColor,1.0),edgecolor='k',lw=2,zorder=200000) ## plot circle, edge coloured inversely from main colour

    ax.set_ylim(-60,90)


    lines = [ [(-15,0), (16.430973, 13.373588)],     # "Africa"
              [(-110,0), (-86.506117, 13.031318)],   # "Americas"
              [(160,30), (105.310561, 31.770208)],   # "EastSouthAsia"
              [(-40,40), (14.323098, 49.012654)],    # "Europe"
              [(75,-1), (59., 40.0)] ]               # "WestCentralAsia"

    ### Africa
    textstr = '\n'.join((
    f"HBV-A: 54",
    f"HBV-D: 53",
    f"HBV-E: 159"))

    ax.text(lines[0][0][0], lines[0][0][1]-1, textstr, fontsize=14,
        verticalalignment='top', horizontalalignment='center' )

    ### Americas
    textstr = '\n'.join((
    f"HBV-A: 236",
    f"HBV-D: 287",
    f"HBV-E: 2"))

    ax.text(lines[1][0][0], lines[1][0][1]-1, textstr, fontsize=14,
        verticalalignment='top', horizontalalignment='center' )

    ### EastSouthAsia
    textstr = '\n'.join((
    f"HBV-A: 62",
    f"HBV-D: 226",
    f"HBV-E: 0"))

    ax.text(lines[2][0][0], lines[2][0][1]-1, textstr, fontsize=14,
        verticalalignment='top', horizontalalignment='center' )

    ### Europe
    textstr = '\n'.join((
    f"HBV-A: 234",
    f"HBV-D: 118",
    f"HBV-E: 73"))

    ax.text(lines[3][0][0], lines[3][0][1]-1, textstr, fontsize=14,
        verticalalignment='top', horizontalalignment='center' )

    ### WestCentralAsia
    textstr = '\n'.join((
    f"HBV-A: 1",
    f"HBV-D: 85",
    f"HBV-E: 0"))

    ax.text(lines[4][0][0], lines[4][0][1]-1, textstr, fontsize=14,
        verticalalignment='top', horizontalalignment='center' )

    lc = mc.LineCollection(lines, colors='k', linewidths=2)
    ax.add_collection(lc)



    ax.set_axis_off()


if __name__ == '__main__':

    folder = "figures"
    output = "static_map_with_counts"
    geojson = "metadata/world.geo.json"

    cmap = { 'europe' : 'indianred',
             'eastsouthasia' : 'steelblue',
             'westcentralasia' : 'mediumpurple',
             'americas' : 'goldenrod',
             'africa' : 'yellowgreen' }
    # set color color_palette
    map_ar = (.62,.3) # aspect ratio of map inset
    map_scale = 25 # scale of map inset
    my_dims=(map_scale*map_ar[0], map_scale*map_ar[1])
    fig, ax =  plt.subplots(figsize=my_dims, dpi=600)
    add_static_map(geojson,cmap,ax)
    plt.savefig(f"{folder}/{output}.pdf",format='pdf')
