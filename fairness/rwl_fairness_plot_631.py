import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import math

color_styles = ['#d73027', '#f46d43', '#2c7bb6', '#fdae61', '#fee090', '#ffffbf', '#e0f3f8', '#abd9e9', '#74add1',
                '#4575b4']
markers = ['x', 'o', '>', 'square', '*', '<']
linestyles = ['solid', 'dashed', 'dashdot', 'dotted']
client_labels = ['B, burst=4000', 'R, rserve=1000', 'BE']


if __name__ == '__main__':
    plt.rc('font', family='Arial')
    labels = ['Matching configuration', 'Limit configuration', 'Weight configuration']
    methods = ['', 'Reservation App', 'Burst App', 'Best-effort App', '']
    x = np.arange(len(methods))  # the label locations
    x = [0, 0.6, 2, 3, 3.6]
    width = 0.2  # the width of the bars
    fig, ax = plt.subplots()
    ax2 = ax.twinx()

    reserve = [24258.0, 27425.0, 39498.0]; rx = [1 - width, 1, 1+width]
    burst = [73.0, 62, 66.0]; bx = [2 - width, 2, 2+width]
    best = [98.0, 98.0, 98.0]; bex = [3 - width, 3, 3+width]

    rx = np.array([0.6])
    rg1 = [30198.0]
    rg2 = [25984.0]
    rg3 = [27054.0]
    rects1 = ax.bar(rx - width, rg1, width, color='#93cf93', hatch='//', edgecolor='black', label=labels[0])
    rects1 = ax.bar(rx, rg2, width, color='#eb9192', hatch='oo', edgecolor='black', label=labels[1])
    rects1 = ax.bar(rx + width, rg3, width, color='#f2bae0', hatch='--', edgecolor='black', label=labels[2])

    gx = np.array([2, 3])
    g1 = [59, 105.0]
    g2 = [71, 107.0]
    g3 = [71.0, 106.0]

    rects1 = ax2.bar(gx - width, g1, width, color='#93cf93', hatch='//', edgecolor='black', label=labels[0])
    rects2 = ax2.bar(gx, g2, width, color='#eb9192', hatch='oo', edgecolor='black', label=labels[1])
    rects3 = ax2.bar(gx + width, g3, width, color='#f2bae0', hatch='--', edgecolor='black', label=labels[2])
    ax.set_ylabel('$95^{th}$ Latency($\mu$s)', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(methods)
    ax2.set_ylabel('Complete Time(s)', fontsize=14)
    # ax2.set_xticks(x)

    ax.legend(ncol=3, loc='upper center', bbox_to_anchor=(0.5, 1.15))

    # ax.yaxis.set_major_locator(plt.MultipleLocator(50))
    plt.grid(axis="y")
    fig.tight_layout()

    plt.savefig("envy_free_rwl.svg")
    plt.show()
