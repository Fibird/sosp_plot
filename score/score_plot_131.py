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

    plot_datas = get_data_from_csv('./131_score.csv')
    baseline = [1.0, 113.0, 120.0, 22285.0]

    labels = ['Burst application', 'Reservation application', 'Best-effort application', 'Total']
    methods = ['R2B', 'R+W', 'R+L', 'W+L', 'R+W+L', 'R', 'W', 'L']
    x = np.arange(len(methods))  # the label locations

    width = 0.2  # the width of the bars
    fig, ax = plt.subplots()

    reserve = []
    burst = []
    best = []
    total = []
    for data in plot_datas:
        reserve.append(data[0] + baseline[3] / data[3])
        burst.append(baseline[1] / data[1])
        best.append(baseline[2] / data[2])
        total.append(data[0] + baseline[3] / data[3] + baseline[1] / data[1] + baseline[2] / data[2])

    rects1 = ax.bar(x - 1.5 * width, burst, width, color='#a6cee3', hatch='//', edgecolor='black', label=labels[0])
    rects2 = ax.bar(x - width * 0.5, reserve, width, color='#1f78b4', hatch='oo', edgecolor='black', label=labels[1])
    rects3 = ax.bar(x + width * 0.5, best, width, color='#b2df8a', hatch='--', edgecolor='black',  label=labels[2])
    rects4 = ax.bar(x + width * 1.5, total, width, color='#33a02c', hatch='x', edgecolor='black',  label=labels[3])


    ax.set_ylabel('Score', fontsize=16)
    ax.set_xticks(x)
    ax.set_xticklabels(methods)
    ax.legend(ncol=3, loc='upper center', bbox_to_anchor=(0.5, 1.21))

    # ax.yaxis.set_major_locator(plt.MultipleLocator(50))
    plt.grid(axis='y', color='0.7', linestyle=':')
    fig.tight_layout()

    plt.savefig("131_score.svg")
    plt.show()
