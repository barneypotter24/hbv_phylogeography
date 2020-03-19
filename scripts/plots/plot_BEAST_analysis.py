import os
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

def convert_partial_year(number):
    year = int(number)
    d = timedelta(days=(number - year)*(365 + is_leap(year)))
    day_one = datetime(year,1,1)
    date = d + day_one
    return date.date().isoformat()

def is_leap(x):
    if x=='2019':
        return False
    else:
        return True

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

def plot_tmrca_kde(log,ax):
    sns.kdeplot(log['age(root)'],shade=True,color='grey',legend=False,ax=ax)
    ax.get_yaxis().set_ticks([])
    yl = max(ax.get_ylim())
    ax.set_ylim(0,yl+50)
    ax.get_yaxis().set_ticks([])

def plot_tip_labels(tre,ax):
    tips = tips = tre.getExternal()
    text_func_tips=lambda k: k.name.split("|")[1]
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

def clock_rate_plot(log,ax):
    sns.boxenplot(log['meanRate'],orient="vertical",color='steelblue',ax=ax)
    ax.axes.set_ylabel("rate (substitutions/site/year)",fontsize=12)
    ax.set_title('Evolutionary rate',fontsize=12)

def add_tmrca_text(log,ax):
    mean_tmrca = convert_partial_year(log['age(root)'].mean())
    tmrca_hpd = [convert_partial_year(x) for x in hpd(log['age(root)'].values,credible_interval=0.95)]
    mean_clock = '%.2E' %log['meanRate'].mean()
    clock_hpd = ['%.2E' %x for x in hpd(log['meanRate'].values,credible_interval=0.95)]
    ax.text(ax.get_xlim()[0]+0.02,ax.get_ylim()[1]*0.6 ,
             f"TMRCA: {(mean_tmrca)}\n\nHPD95%: {tmrca_hpd[0]} to {tmrca_hpd[1]}",fontsize=15)
    ax.text(ax.get_xlim()[0]+0.02,ax.get_ylim()[1]*0.5 ,
             f"Clock rate: {mean_clock}\n\nHPD95%: {clock_hpd[0]} to {clock_hpd[1]}",fontsize=15)

def add_legend(color_dict, ax):
    legend_elements = []
    for name,clr in color_dict.items():
        dot = Line2D([0], [0], marker='o', color='w', label=name,
                          markerfacecolor=clr, markersize=15)
        legend_elements.append(dot)
    ax.invert_yaxis()
    ax.ticklabel_format(useOffset=False, style='plain')
    ax.legend(handles=legend_elements, loc='lower left',fontsize=12,frameon=False)

def plot_BEAST(tre,log,o_file):
    # set color color_palette
    country_color = set_country_colors(tre)
    # add tree plot
    fig,ax =  plt.subplots(figsize=(15,15))
    # set x axis to be time
    x_attr=lambda k: k.absoluteTime
    tre.plotTree(ax=ax,x_attr=x_attr, branchWidth=lambda x: 1)
    mrsd = max([x.absoluteTime for x in tre.getExternal()])
    ax.set_xlim(log['age(root)'].mean()-0.3,mrsd+0.2)
    # color tips by country
    point_color = lambda k: country_color[k.name.split("|")[-2]]
    tre.plotPoints(ax=ax,x_attr=x_attr,colour_function=lambda x: 'k', # tip shape outline
                   size_function=lambda x:100)
    tre.plotPoints(ax=ax,x_attr=x_attr,colour_function=point_color,
                   size_function=lambda x:70,)
    # add indicator for posterior support
    text_func=lambda k: "⁎" if k.traits['posterior']>0.5 else ""
    text_pos_func=lambda k: (k.absoluteTime,k.y+0.2)
    target_func=lambda k: k.branchType=='node' ## only target nodes
    tre.addText(ax,position=text_pos_func,target=target_func,text=text_func,size=15,color='black',weight='bold')
    ax.annotate('⁎ indicates nodes with posterior>0.5  ', xy=(1, 0), xycoords='axes fraction', fontsize=12,
                horizontalalignment='right', verticalalignment='bottom')
    # plot aligned tip labels
    plot_tip_labels(tre,ax)
    # plot legend
    add_legend(country_color,ax)
    # plot tmrca kde on twin x axis
    ax2 = ax.twinx()
    plot_tmrca_kde(log,ax2)
    #plot clock rate boxplot
    inside = plt.axes([.20, .65, .1, .2])
    clock_rate_plot(log,inside)
    #plot time to ancestors boxplot
    inside2 = plt.axes([.35, .65, .1, .2])
    time_delta_plot(tre,inside2)
    # add tmrca dates text
    add_tmrca_text(log,ax2)
    # add title
    epi_day = o_file.split('/')[-1].replace('arambaut.','').replace('.pdf','')
    ax.set_title( f"2019-nCoV BEAST analysis ({epi_day})",fontsize=20 )

    # export to pdf
    plt.savefig(o_file,format='pdf')

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--folder',help='Folder with BEAST run', default=".")
    parser.add_argument('--filestem',help='file stem of BEAST run ')
    parser.add_argument('--output',help='output plot file name')
    parser.add_argument('--burnin',type=int,help='burnin',default=2000000)
    args = parser.parse_args()

    trees_file = f"{args.folder}/{args.filestem}.trees"
    log_file = f"{args.folder}/{args.filestem}.log"
    # plot tree
    mcc_tree = bt.loadNexus(f"{args.folder}/{args.filestem}.mcc.tre",variableDate=True,tip_regex='\/([\-0-9]+)',date_fmt='%Y',)
    log = pd.read_csv(log_file,sep='\t',skiprows=3,index_col=0)
    log = log.loc[args.burnin:].copy()
    plot_file = f"{args.folder}/{args.output}.pdf"
    plot_BEAST(mcc_tree,log,plot_file)
