import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import math
from matplotlib import gridspec

color_styles = ['#d73027', '#f46d43', '#2c7bb6', '#fdae61', '#fee090', '#ffffbf', '#e0f3f8', '#abd9e9', '#74add1', '#4575b4']
markers = ['x', 'o', '>', 'square', '*', '<']
linestyles = ['solid', 'dashed', 'dashdot', 'dotted']
client_labels = ['Burst Application', 'Reservation Application', 'Best-effort Application']

def io_plot(save_img=False):
    font_name = 'Arial'
    font_size = 16
    font1 = {'family': font_name,
             'weight': 'normal',
             'size': font_size,
             }
    fig = plt.figure(figsize=(16, 0.5))
    ax1 = fig.add_subplot(111)

    for i in range(3):
        ax1.plot([-1], [-1], linewidth=2, color=color_styles[i], linestyle=linestyles[i], marker=markers[i], label=client_labels[i])

    ax1.plot([-1], [-1], linewidth=2, color='black', label='system utilization')

    ax1.legend(ncol=4, loc='center', prop=font1, framealpha=1.0, edgecolor='black')
    plt.axis('off')
    fig.tight_layout()

    if save_img:
        plt.savefig("alone_legend.svg")
    plt.show()


if __name__ == '__main__':
    io_plot(True)
