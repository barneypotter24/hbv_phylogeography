'''plot_ml_trees.py'''

import math

import baltic as bt
import matplotlib as mpl
import matplotlib.pyplot as plt
from argh import dispatch_command
from matplotlib.lines import Line2D


def main() -> None:
    genotypes = ['A', 'D', 'E']
    # genotypes = ['A']
    for genotype in genotypes:
        print(f"Starting Genotype {genotype}")
        folder = f"ml/{genotype}"
        filestem = f"HBV-{genotype}_ML"
        output = f"HBV-{genotype}_ML"

        # plot tree
        ml_tree = bt.loadNewick(f"{folder}/{filestem}.nwk",
                                variableDate=True,
                                tip_regex='\/([\-0-9]+)',
                                date_fmt='%Y',)

        print(ml_tree.treeStats())
        plot_file = f"figures/{output}.pdf"

        ms = set()
        for k in ml_tree.Objects:
            if k.branchType=='leaf':
                if k.name in ms:
                    print(f"BAD: {k.name}")
                else:
                    ms.add(k.name)

        cmap_map = {
            "A": 'tab20',
            "D": 'tab20b',
            "E": 'tab20c'
        }
        cmap = mpl.cm.get_cmap(cmap_map[genotype], 10)

        fig, ax = plt.subplots(figsize=(15, 15), dpi=600)
        # set x axis to be time
        # box_size = 1.05

        fc = ((.99, .99, .99))
        ax.set_facecolor(fc)

        plot_ml_tree(ml_tree, ax, cmap, genotype)
        # ax.set_xlim(-box_size, box_size)
        # ax.set_ylim(-box_size, box_size)
        ax.set_axis_off()
        # fig.suptitle( f"HBV-{genotype} new sequences",fontsize=20 )
        plt.tight_layout()
        # export to pdf
        plt.savefig(plot_file,format='pdf')

        # export to png
        plt.savefig(plot_file.replace('.pdf','.png'), format='png')


def plot_ml_tree(tre, ax, cmap, gt):

    r = 8

    cdict = {}
    p_t_func = lambda x: (x.branchType=='leaf' and x.absoluteTime > tcutoff)
    c_func = lambda x: extract_subgenotype_to_color(x,cmap,cdict,gt)
    p_c_func = lambda x: extract_subgenotype_to_color(x,cmap,cdict,gt) if not is_new_sequence(x) else 'k'
    p_o_func = lambda x: 40 if is_new_sequence(x) else 6
    p_i_func = lambda x: 27 if is_new_sequence(x) else 4
    w_func = lambda x: 1.
    z_func_lines = lambda x: 800 if is_new_sequence(x) else 300
    z_func_p_o = lambda x: 900 if is_new_sequence(x) else 400
    z_func_p_i = lambda x: 1000 if is_new_sequence(x) else 500

    ######################
    ##### tree  plot #####
    ######################
    tre.plotTree(ax=ax,
                         colour=c_func,
                         width=w_func,
                         zorder=300)

    tre.plotPoints(ax=ax,
                           colour=p_c_func,
                           size=p_i_func,
                           outline_size=p_o_func,
                           outline_colour='k',
                           zorder=400)

    # plot_tip_labels(tre, ax)
    add_legend(cdict, ax)

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
    return 'grey'


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
              loc='lower left',
              # bbox_to_anchor=(0.51,0.5),
              fontsize=12,
              frameon=False)


def is_new_sequence(x):
    if x.branchType == 'leaf':
        if 'MB' in x.name.split('/')[1]:
            return True
    else:
        return False

def plot_tip_labels(tre, ax):
    text_func = lambda k: '*'
    target_func = lambda k: is_new_sequence(k)
    xf = lambda k: k.x - .0003
    yf = lambda k: k.y - 3.1

    for k in filter(target_func, tre.Objects):
        X = xf(k)
        Y = yf(k)

        ax.text(X,Y,
                text_func(k),
                zorder=1000,
                size=10)



if __name__=="__main__":
    dispatch_command(main)
