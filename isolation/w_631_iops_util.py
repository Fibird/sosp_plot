import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import math
from matplotlib import gridspec

color_styles = ['#d73027', '#f46d43', '#2c7bb6', '#fdae61', '#fee090', '#ffffbf', '#e0f3f8', '#abd9e9', '#74add1', '#4575b4']
markers = ['x', 'o', '>', 'square', '*', '<']
linestyles = ['solid', 'dashed', 'dashdot', 'dotted']
client_labels = ['B: w=6', 'R: w=3', 'BE: w=1']


def get_data_from_sim(file_name):
    data = []
    f = open(file_name)
    for index, line in enumerate(f):
        line_list = line.split()
        cols = len(line_list)
        if index == 0:
            for i in range(cols - 1):
                data.append([])
        if index > 0:
            for i in range(0, cols - 1):
                data[i].append(float(line_list[i + 1]))

    f.close()
    return data


def io_plot(plot_data, save_img=False):
    # fig = plt.figure(figsize=(8, 6))
    # ax = fig.add_subplot(111)

    # fig = plt.figure()
    # set height ratios for subplots
    fig, axes = plt.subplots(nrows=2, ncols=1, sharex='col',
                             gridspec_kw={'height_ratios': [2, 1]},
                             figsize=(8, 6))
    # gs = gridspec.GridSpec(2, 1, height_ratios=[2, 1])

    # the first subplot
    # ax = plt.subplot(gs[0])
    ax1 = axes[0]
    ax2 = axes[1]
    xs = np.arange(0, len(plot_data[0]), 1)
    reserve_line = np.ones(len(xs)) * 1200
    count = 0
    for ys in plot_data:
        if count < (len(plot_data) - 1):
            ax1.plot(xs, ys, linewidth=1, color=color_styles[count], linestyle=linestyles[count], marker=markers[count], label=client_labels[count])
        count = count + 1

    ax1.plot([-1], [-1], linewidth=1, color='black', label='system utilization')

    count = 3
    # ax2 = plt.subplot(gs[1], sharex=ax)
    utils = np.array(plot_data[count]) / 5100
    ax2.plot(xs, utils, linewidth=1, color='black', label='system utilization')

    ax1.axhline(1200, linestyle=':', linewidth=1, color='k')

    # ax.xaxis.set_major_locator(plt.MultipleLocator(50))
    #ax.yaxis.set_major_locator(plt.MultipleLocator(10))
    ax1.set(xlim=(0, len(xs) - 1), ylim=(0, 5200))
    ax1.tick_params(direction='in')
    ax2.tick_params(direction='in')
    ax1.grid(axis='y', color='0.7', linestyle=':')
    # ax.legend(loc='center right')

    font1 = {'family': 'Arial',
             'weight': 'normal',
             # 'size': 14,
             }

    ax1.legend(ncol=4, loc='upper center', bbox_to_anchor=(0.5, 1.15))
    # plt.yticks(list(plt.yticks()[0]) + [1200])

    ax2.set_xlabel("Time (sec)", font1)
    ax1.set_ylabel("IOPS", font1)
    ax2.set_ylabel("System Utilization", font1)
    fig.tight_layout()

    labels = ax1.get_xticklabels() + ax1.get_yticklabels() + ax2.get_xticklabels() + ax2.get_yticklabels()
    [label.set_fontname('Arial') for label in labels]

    plt.grid(axis='y', color='0.7', linestyle=':')
    # plt.setp(ax1.get_xticklabels(), visible=False)
    plt.subplots_adjust(hspace=.0)
    if save_img:
        date_str = datetime.now().strftime("%y%m%d%H%M%S")
        plt.savefig("w_631_iops.svg")
    plt.show()


if __name__ == '__main__':
    data = get_data_from_sim("../logs/w_631_iops.log")
    io_plot(data, True)
