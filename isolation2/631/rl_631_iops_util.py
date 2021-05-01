import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import math
from matplotlib import gridspec

color_styles = ['#d73027', '#f46d43', '#2c7bb6', '#fdae61', '#fee090', '#ffffbf', '#e0f3f8', '#abd9e9', '#74add1', '#4575b4']
markers = ['x', 'o', '>', 'square', '*', '<']
linestyles = ['solid', 'dashed', 'dashdot', 'dotted']
client_labels = ['B: r=3000,l=5000', 'R: r=1200,l=2000', 'BE: r=0,l=500']


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
    font_name = 'Arial'
    font_size = 18
    fig, axes = plt.subplots(nrows=2, ncols=1, sharex='col',
                             gridspec_kw={'height_ratios': [2, 1]},
                             figsize=(8, 5))
    ax1 = axes[0]
    ax2 = axes[1]
    xs = np.arange(0, len(plot_data[0]), 1)
    reserve_line = np.ones(len(xs)) * 1200
    count = 0
    for ys in plot_data:
        if count < (len(plot_data) - 1):
            ax1.plot(xs, ys, linewidth=1, color=color_styles[count], linestyle=linestyles[count], marker=markers[count], label=client_labels[count])
        count = count + 1

    count = 3
    # ax2 = plt.subplot(gs[1], sharex=ax)
    utils = np.array(plot_data[count]) / 5100
    ax2.plot(xs, utils, linewidth=1, color='black', label='system utilization')
    ax2.fill_between(xs, 0, utils, alpha=.3)
    ax1.axhline(1200, linestyle=':', linewidth=1, color='k')

    ax1.set(xlim=(0, 130), ylim=(0, 5200))
    ax1.tick_params(direction='in', labelsize=16)
    ax2.tick_params(direction='in', labelsize=16)
    ax1.grid(axis='y', color='0.7', linestyle=':')

    font1 = {'family': font_name,
             'weight': 'normal',
             'size': font_size,
             }

    # plt.yticks(list(plt.yticks()[0]) + [1200])

    ax2.set_xlabel("Time (sec)", font1)
    ax1.set_ylabel("IOPS", font1)
    ax2.set_ylabel("System Utilization", font1)
    fig.tight_layout()

    labels = ax1.get_xticklabels() + ax1.get_yticklabels() + ax2.get_xticklabels() + ax2.get_yticklabels()
    [label.set_fontname(font_name) for label in labels]

    plt.grid(axis='y', color='0.7', linestyle=':')
    # plt.setp(ax1.get_xticklabels(), visible=False)
    plt.subplots_adjust(hspace=.0)

    if save_img:
        date_str = datetime.now().strftime("%y%m%d%H%M%S")
        plt.savefig("rl_631_iops.svg")
    plt.show()


if __name__ == '__main__':
    data = get_data_from_sim("rl2_iops.log")
    io_plot(data, True)
