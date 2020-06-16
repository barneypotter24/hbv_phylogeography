'''plot_markov_jumps.py'''
import sys
from math import sin, cos, pi
from utils import *
import matplotlib.pyplot as plt
import matplotlib.colors as col

def get_mj_minmax(markov_jump_map):
    all_mjs = []
    for f in markov_jump_map:
        for t in markov_jump_map[f]:
            all_mjs.append(markov_jump_map[f][t])
    return (min(all_mjs),max(all_mjs))

def configure_axis(ax,label):
    ax.set_xlim(-1.3,1.3)
    ax.set_ylim(-1.3,1.3)
    ax.set_axis_off()
    ax.set_title(label)

def plot_bezier(ax,markov_jump_map,point_locations):
    cmap_name='Blues'
    cmap=mpl.cm.get_cmap(cmap_name)
    mjmin,mjmax = get_mj_minmax(markov_jump_map)
    for f in markov_jump_map.keys(): ## iterate through members of maps.keys()
        for t in markov_jump_map[f].keys():

            desX,desY=point_locations[t] ## get point coordinates
            oriX,oriY=point_locations[f]

            mj_norm=markov_jump_map[f][t]/mjmax ## normalize markov jumps

            distance=math.sqrt(math.pow(oriX-desX,2)+math.pow(oriY-desY,2)) ## find travelling distance

            # adjust_d=-math.sqrt(.2*distance) ## position Bezier curve control point according to an arbitrary function
            adjust_d=-.2

            n=Bezier_control((oriX,oriY),(desX,desY),adjust_d) ## control point perpendicular to midway between point A and B at a distance adjust_d

            curve=Bezier([(oriX,oriY),n,(desX,desY)],0.0,1.0,num=30) ## get Bezier line coordinates

            for i in range(len(curve)-1): ## iterate through Bezier curve coordinates, alter colour according to height
                x1,y1=curve[i]
                x2,y2=curve[i+1]
                frac=i/float(len(curve)) ## fraction along line

                ax.plot([x1,x2],[y1,y2],
                        lw=1+4*(1-frac),
                        color=cmap(mj_norm),
                        zorder=10) ## curve tapers and changes colour

def determine_point_locations(locations, offset=0.):
    '''
    take a list of locations, return a dictionary of (x,y) tuple
        coordinates for where each location should be plotted on a circle

    Each coordinate is determined according to:

    (x,y) = (cos(theta),sin(theta))

    such that

    theta = (n*2*pi)/N + phi

    where

    n = index of current point in the list
    N = total number of items in the list
    phi = some offset (in radians)
    '''
    # Initialize empty dictionary that will store the mapping
    coord_dictionary = {}

    N = len(locations)

    getTheta = lambda x,X: ((2*x*pi)/X)
    for n in range(len(locations)):
        theta = getTheta(n,N) + offset
        coord_dictionary[locations[n]] = (cos(theta),sin(theta))
    return coord_dictionary

def determine_alignment_corner(x,y):
    if x>=0:
        ha='left'
    else:
        ha='right'

    if y>=0:
        va='bottom'
    else:
        va='top'

    return ha,va

def get_label_from_loc(loc):
    label = loc
    if label == 'WestCentralAsia':
        label = 'West/Central\nAsia'
    if label == 'EastSouthAsia':
        label = 'East/South\nAsia'
    return label

def plot_points(ax,point_locations,point_size,color_func):
    for loc in point_locations:
        x,y = point_locations[loc]
        ax.scatter(x,y,
                   point_size,
                   facecolor=color_func(loc),
                   edgecolor='k',
                   lw=2,
                   zorder=20) ## plot circle
        lb = 1
        ha,va=determine_alignment_corner(x,y)
        label=get_label_from_loc(loc)
        ax.annotate(label,
                    xy=(x*1.1,y*1.1),
                    zorder=30,
                    ha=ha,
                    va=va,
                    bbox=dict(boxstyle="round",
                                ec=[lb]*3,
                                fc=[lb]*3,
                                alpha=.8)
                   )

def parse_tsv(fname):
    o = {} # initialize some dict
    with open(fname,'r') as f:
        f.readline() # skip the header
        for line in f.readlines(): # go thourgh lines of the txt file
            line=line.strip().split('\t') # split the line
            fr = line[1] # going from
            to = line[2] # going to
            if fr in o.keys():
                if to in o[fr].keys(): # we've seen this combo before
                    o[fr][to] += 1
                else: # we haven't, so we set the jump count to 1
                    o[fr][to] = 1
            else: # haven't seen "from" before, so we add to=1
                o[fr] = {to: 1}
            if to not in o.keys():
                o[to] = {fr: 0}
    return o

def add_colorbar(fig,ax,markov_jump_map,cbs):
    mjmin,mjmax = get_mj_minmax(markov_jump_map)

    colorbarTextSize=15 ## add colourbars
    colorbarTickLabelSize=12
    colorbarWidth=0.02
    colorbarHeight=0.35

    colorbar_xcoord = 0.49+(0.421*(len(cbs)%2))
    colorbar_ycoord = 0.53-(0.42*(len(cbs)//2))


    cbs.append(fig.add_axes([colorbar_xcoord,
                             colorbar_ycoord,
                             colorbarWidth,
                             colorbarHeight])) ## add dummy axes

    cbar = mpl.colorbar.ColorbarBase(cbs[-1],
                                   cmap=mpl.cm.get_cmap('Blues'),
                                   orientation='vertical')
    cbs[-1].yaxis.set_major_locator(mpl.ticker.LinearLocator(numticks=mjmax+1)) ## add colour bar to axes

    yaxis_labels=[str(i) for i in range(mjmax+1)]

    cbs[-1].set_yticklabels(yaxis_labels) #


def create_markov_jump_subplot(fig,ax,mjm,label,color_func,cbs,psize=200):
    locations = list(mjm.keys())
    point_coords = determine_point_locations(locations,offset=(pi/(len(locations))))
    plot_points(ax,point_coords,psize,color_func)
    plot_bezier(ax,mjm, point_coords)
    add_colorbar(fig,ax,mjm,cbs)
    configure_axis(ax,label)

if __name__ == "__main__":

    mj_files = [ 'phylogeography/a/mjr/jumpTimes.txt',
                 'phylogeography/d/mjr/jumpTimes.txt',
                 'phylogeography/e/mjr/jumpTimes.txt' ]
    labels = ['HBV-A including ancient genomes',
              'HBV-D including ancient genomes',
              'HBV-E']
    assert len(mj_files) <= 4, "Too many markov jump analyses to plot"

    fig, ((ax0,ax1),(ax2,ax3)) =  plt.subplots(nrows=2,
                                           ncols=2,
                                           sharex=True,
                                           sharey=True,
                                           figsize=(15,15),
                                           dpi=600)
    axs = [ax0,ax1,ax2,ax3] # There is probably some nicer python to do this
    cbs=[]
    cdict = { 'europe' : 'indianred',
              'eastsouthasia' : 'steelblue',
              'westcentralasia' : 'mediumpurple',
              'americas' : 'goldenrod',
              'africa' : 'yellowgreen' }
    for i in range(len(mj_files)):
        mj_dict = parse_tsv(mj_files[i])
        colors = lambda k: cdict[k.lower()]
        create_markov_jump_subplot(fig,axs[i],mj_dict,labels[i],colors,cbs)

    configure_axis(ax3,'')
    plt.savefig('phylogeography/markov_jumps.png')
