import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import math

color_styles = ['#d73027', '#f46d43', '#2c7bb6', '#fdae61', '#fee090', '#ffffbf', '#e0f3f8', '#abd9e9', '#74add1',
                '#4575b4']
markers = ['x', 'o', '>', 'square', '*', '<']
linestyles = ['solid', 'dashed', 'dashdot', 'dotted']

def get_data_from_csv(file_name):
    data = []
    f = open(file_name)
    for index, line in enumerate(f):
        line_list = line.split(',')
        if index != 0:
            tmp = []
            for d in line_list[1:]:
                tmp.append(float(d))
            data.append(tmp)


    f.close()
    return data

if __name__ == '__main__':
    plt.rc('font', family='Arial')

    plot_datas = get_data_from_csv('./121_score.csv')
    baseline = [1.0, 113.0, 120.0, 22285.0]

    labels = ['Burst application', 'Reservation application', 'Best-effort application', 'Total']
    methods = ['R', 'R+L', 'L', 'R+W+L', 'W+L', 'R2B', 'R+W', 'W']
    x = np.arange(len(methods))  # the label locations

    width = 0.5  # the width of the bars
    fig, ax = plt.subplots(figsize=(4, 5))

    reserve = []
    burst = []
    best = []
    total = []
    for data in plot_datas:
        best.append(baseline[2] / data[2])

    best.sort()

    rects1 = ax.barh(x, best, width, color='#a6cee3', edgecolor='black')
    # rects2 = ax.barh(x - width * 0.5, reserve, width, color='#1f78b4', hatch='oo', edgecolor='black', label=labels[1])
    # rects3 = ax.barh(x + width * 0.5, best, width, color='#b2df8a', hatch='--', edgecolor='black',  label=labels[2])
    # rects4 = ax.barh(x + width * 1.5, total, width, color='#33a02c', hatch='x', edgecolor='black',  label=labels[3])


    ax.set_yticks(x)
    ax.xaxis.set_ticks_position('top')
    ax.set_yticklabels(methods)
    ax.set_xlabel('Score', fontsize=16)
    ax.set(xlim=(0.3, 0.8))
    # ax.legend(ncol=3, loc='upper center', bbox_to_anchor=(0.5, 1.21))

    # ax.yaxis.set_major_locator(plt.MultipleLocator(50))
    plt.grid(axis='x', color='0.7', linestyle=':')
    fig.tight_layout()

    plt.savefig("131_best_score.svg")
    plt.show()
