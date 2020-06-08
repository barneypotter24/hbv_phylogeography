'''plot_new_sequences.py
'''
import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import baltic.baltic as bt
import pandas as pd
import math
import re

def main():
    genotypes = ['A']
    # genotypes = ['D']
    for genotype in genotypes:
        print(f"Starting Genotype {genotype}")
        folder = f"phylogeography/{genotype.lower()}"
        filestem = f"HBV-{genotype}_phylogeography"
        log = f"beast_files/{genotype.lower()}/combined/HBV-{genotype}_combined.log"
        output = f"HBV-{genotype}_new_sequences"
        burnin = 0
        geojson = "metadata/world.geo.json"

        trees_file = f"{folder}/{filestem}.trees"
        log_file = log
        # plot tree
        mcc_tree = bt.loadNexus(f"{folder}/{filestem}.mcc.tre",variableDate=True,tip_regex='\/([\-0-9]+)',date_fmt='%Y',)
        threshold = 1000
        no_ancient = lambda x: False if (x.branchType=="leaf" and x.absoluteTime < threshold) else True
        ci = lambda x: True if (x.branchType=='node' and len(x.children)<2) else False
        mySubtree = mcc_tree.subtree(k=determine_the_correct_node(mcc_tree.root),
                                     traverse_condition=no_ancient).collapseBranches(collapseIf=ci)
        if genotype=='D':
            mySubtree.root.absoluteTime += 1300
        mySubtree.ySpan = max([n.y for n in mySubtree.getExternal()])-min([n.y for n in mySubtree.getExternal()])
        print("Root time of total tree:")
        print(mcc_tree.root.absoluteTime)
        print("Root time of mySubtree:")
        print(mySubtree.root.absoluteTime)
        plot_file = f"figures/{output}.pdf"

        cmap_map = {
            "A" : 'tab20',
            "D" : 'tab20b',
            "E" : 'tab20c'
        }
        cmap = mpl.cm.get_cmap(cmap_map[genotype],10)

        fig, ax =  plt.subplots(figsize=(15,15), dpi=300)
        # set x axis to be time
        x_attr=lambda k: k.absoluteTime

        box_size=1.05

        fc = ((.99,.99,.99))
        ax.set_facecolor(fc)

        plot_BEAST_tree(mySubtree,log,ax,cmap,genotype)
        ax.set_xlim(-box_size,box_size)
        ax.set_ylim(-box_size,box_size)
        ax.set_axis_off()

        fig.suptitle( f"HBV-{genotype} new sequences",fontsize=20 )

        # export to pdf
        plt.savefig(plot_file,format='pdf')

        # export to png
        plt.savefig(plot_file.replace('.pdf','.png'), format='png')

def determine_the_correct_node(n):
    '''recursively look for the first node who only has internal nodes as children'''
    amItheOne = True # DJ Khaled would be impressed
    for child in n.children:
        if child.branchType=='leaf':
            amItheOne = False # If any of my kids are leaves we're gonna have a problem
    if amItheOne:
        return n
    else:
        for child in n.children:
            if child.branchType=='node': #don't bother with leaves
                return determine_the_correct_node(child)

def is_new_sequence(x):
    if x.branchType == 'leaf':
        if 'MB' in x.name.split('/')[1]:
            return True
    else:
        return False

def determine_subtype(x):
    if len(x.name.split('/')[0]) > 1:
        return x.name.split('/')[0][-1]
    else:
        return '0'

def extract_subgenotype_to_color(x,cmap,cdict,gt):
    if x.branchType == 'leaf': # only leaves can have subgenotopes
        n = x.name.split('/')[0]
        if len(n) > 1 and n[0] == gt:
            n0 = n[1:]
            try:
                cdict[f"Subgenotype {n0}"] = cmap(int(n0))
                return cmap(int(n0))
            except:
                if n0 == 'D':
                    cdict["Subgenotype 4"] = cmap(9)
                    return cmap(9)
                else:
                    print('BAD:',n0)
                    return 'red'
        cdict['Uncategorized'] = 'grey'
        return 'grey'
    return 'k'


def plot_tip_labels(tre,ax,circFrac=1.0):
    circStart=0.0
    text_func=lambda k: k.name
    # text_pos_func =lambda k: (0,0)
    target_func=lambda k: is_new_sequence(k)
    circ_s=circStart*math.pi*2
    circ=circFrac*math.pi*2

    normaliseHeight=lambda value,values: (value-min(values))/(max(values)-min(values))
    linspace=lambda start,stop,n: list(start+((stop-start)/(n-1))*i for i in range(n)) if n>1 else stop
    x_attr=lambda x: x.absoluteTime
    y_attr=lambda x: x.y
    value_range=list(map(x_attr,tre.Objects))

    c = 0
    dist = 1.025
    for k in filter(target_func,tre.Objects):

        y=circ_s+circ*y_attr(k)/tre.ySpan ## get y position along circle's perimeter
        theta = (90 - math.degrees(y))%360
        X=dist*math.cos(math.radians(theta)) ## transform
        Y=dist*math.sin(math.radians(theta)) ## transform

        if X>0:
            h_aln='left'
        else:
            h_aln='right'

        if Y>0:
            v_aln='bottom'
        else:
            v_aln='top'

        txt_rotation = 180+theta if X<0 else theta


        ax.text(X,Y,
                text_func(k),
                zorder=1000,
                ha=h_aln,
                va=v_aln,
                rotation=txt_rotation,
                size=5)
        c += 1
    print("Total labels:",c)

    # plot dash to labels
    # for tip in tips:
    #     x = [tip.absoluteTime,tip_label_pos]
    #     y= [tip.y,tip.y]
    #     ax.plot(x,y,linestyle=':',color='grey')

def add_legend(color_dict, ax):
    if len(color_dict.keys()) < 2:
        return
    md = {}
    for name,clr in color_dict.items():
        dot = Line2D([0], [0],
                        marker='o',
                        color='w',
                        label=name,
                        markerfacecolor=clr,
                        markersize=15)
        md[name] = dot
    legend_elements = []
    labels=[]
    for key in sorted(md.keys()):
        legend_elements.append(md[key])
        labels.append(key)
    ax.ticklabel_format(useOffset=False,
                        style='plain')
    ax.legend(handles=legend_elements,
              labels=labels,
              loc='center left',
              bbox_to_anchor=(0.51,0.5),
              fontsize=12,
              frameon=False)

def plot_BEAST_tree(tre,log,ax,cmap,gt):
    r = 8

    cdict = {}
    x_attr=lambda x: x.absoluteTime # x axis is time
    p_t_func = lambda x: (x.branchType=='leaf' and x.absoluteTime > tcutoff)
    c_func = lambda x: extract_subgenotype_to_color(x,cmap,cdict,gt)
    p_o_func = lambda x: 35 if is_new_sequence(x) else 10
    p_i_func = lambda x: 27 if is_new_sequence(x) else 6
    w_func = lambda x: 1.
    z_func_lines = lambda x: 800 if is_new_sequence(x) else 300
    z_func_p_o = lambda x: 900 if is_new_sequence(x) else 400
    z_func_p_i = lambda x: 1000 if is_new_sequence(x) else 500

    ######################
    ##### tree  plot #####
    ######################
    normaliseHeight_func=lambda value,values: (value-min(values))/(max(values)-min(values))

    cf = .9975

    tre.plotCircularTree(ax=ax,
                         x_attr=x_attr,
                         circFrac=cf,
                         colour_function=c_func,
                         branchWidth=w_func,
                         zorder_function=z_func_lines,
                         normaliseHeight=normaliseHeight_func)

    # color tips by country
    tre.plotCircularPoints(ax=ax,
                           x_attr=x_attr,
                           circFrac=cf,
                           colour_function=lambda x: 'k', # tip shape outline
                           size_function=p_o_func,
                           zorder=400)
    tre.plotCircularPoints(ax=ax,
                           x_attr=x_attr,
                           circFrac=cf,
                           colour_function=c_func,
                           size_function=p_i_func,
                           zorder=500)

    plot_tip_labels(tre,ax,cf)
    add_legend(cdict, ax)

    # ax.get_yaxis().set_ticks([])
    ax.xaxis.tick_top()


if __name__ == '__main__':
    main()
