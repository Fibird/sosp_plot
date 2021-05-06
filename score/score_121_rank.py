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
    font_name = 'Arial'
    font_size = 20
    plt.rc('font', family='Arial')

    font1 = {'family': font_name,
             'weight': 'normal',
             'size': font_size,
             }

    plot_datas = get_data_from_csv('./121_score.csv')
    baseline = [1.0, 113.0, 120.0, 22285.0]

    labels = ['Burst application', 'Reservation application', 'Best-effort application', 'Total']

    width = 0.5  # the width of the bars
    fig, axes = plt.subplots(1, 3, figsize=(12, 6))
    # ax0 = axes[0][0]
    # ax1 = axes[0][1]
    # ax2 = axes[1][0]
    # ax3 = axes[1][1]
    ax1 = axes[0]
    ax2 = axes[1]
    ax3 = axes[2]

    reserve = []
    reserve1 = []
    burst = []
    best = []
    total = []
    # for data in plot_datas:
    #     best.append(baseline[2] / data[2])

    for data in plot_datas:
        reserve.append(data[0])
        reserve1.append(data[3])
        burst.append(data[1])
        best.append(data[2])
        # total.append(data[0] + baseline[3] / data[3] + baseline[1] / data[1] + baseline[2] / data[2])

    # methods = ['L', 'R', 'R+L', 'W', 'W+L', 'R+W+L', 'R+W', 'R2B']
    # x = np.arange(len(methods))  # the label locations
    # reserve.sort()
    # rects2 = ax0.barh(x, reserve, width, color='#a6cee3', edgecolor='black')
    # ax0.set_yticks(x)
    # ax0.set_yticklabels(methods)
    # ax0.xaxis.set_ticks_position('top')
    # ax0.tick_params(direction='in', labelsize=font_size)
    # ax0.set_xlabel("Rs' IOPS Score", fontsize=font_size)
    # ax0.set(xlim=(0.7, 1.0))

    methods = ['R', 'R+L', 'L',  'R+W+L', 'W+L', 'R+W', 'R2B', 'W']
    x = np.arange(len(methods))  # the label locations
    reserve1.sort(reverse=True)
    rects2 = ax1.barh(x, reserve1, width, color='#a6cee3', edgecolor='black')
    rects3 = ax1.barh([6], [reserve1[6]], width, color='red', edgecolor='black')
    ax1.set_yticks(x)
    ax1.set_yticklabels(methods)
    ax1.xaxis.set_ticks_position('top')
    ax1.xaxis.set_label_position('top')
    ax1.tick_params(direction='in', labelsize=font_size)
    ax1.set_xlabel("$95^{th}$ Latency(ns)", fontsize=font_size)
    ax1.set(xlim=(20, None))
    ax1.set_title("Ranking of R Application", y=-0.15, fontsize=font_size)
    for a, b in zip(x, reserve1):
        ax1.text(b + 13000 if b < 30000 else b-8000, a - 0.3, '%.1f' % b, ha='center', va='bottom', fontsize=font_size)
    # rects2 = ax.barh(x - width * 0.5, reserve, width, color='#1f78b4', hatch='oo', edgecolor='black', label=labels[1])
    # rects3 = ax.barh(x + width * 0.5, best, width, color='#b2df8a', hatch='--', edgecolor='black',  label=labels[2])
    # rects4 = ax.barh(x + width * 1.5, total, width, color='#33a02c', hatch='x', edgecolor='black',  label=labels[3])

    methods = ['R', 'W', 'W+L', 'R+W+L', 'L', 'R+L', 'R+W', 'R2B']
    x = np.arange(len(methods))  # the label locations
    burst.sort(reverse=True)
    rects2 = ax2.barh(x, burst, width, color='#a6cee3', edgecolor='black')
    strong = ax2.barh([7], [burst[7]], width, color='red', edgecolor='black')
    ax2.set_yticks(x)
    ax2.set_yticklabels(methods)
    ax2.xaxis.set_ticks_position('top')
    ax2.xaxis.set_label_position('top')
    ax2.tick_params(direction='in', labelsize=font_size)
    ax2.set_xlabel("Completion Time(s)", fontsize=font_size)
    ax2.set(xlim=(200, None))
    ax2.set_title("Ranking of B Application", y=-0.15, fontsize=font_size)
    for a, b in zip(x, burst):
        ax2.text(b+18 if b < 300 else b, a - 0.3, '%.1f' % b, ha='center', va='bottom',
                 fontsize=font_size)

    methods = ['R', 'R+L', 'L', 'R+W+L', 'W+L', 'R2B', 'R+W', 'W']
    x = np.arange(len(methods))  # the label locations
    best.sort(reverse=True)
    rects1 = ax3.barh(x, best, width, color='#a6cee3', edgecolor='black')
    rects1 = ax3.barh([5], [best[5]], width, color='red', edgecolor='black')
    ax3.set_yticks(x)
    ax3.set_yticklabels(methods)
    ax3.xaxis.set_ticks_position('top')
    ax3.xaxis.set_label_position('top')
    ax3.tick_params(direction='in', labelsize=font_size)
    ax3.set_xlabel("Completion Time(s)", fontsize=font_size)
    ax3.set(xlim=(100, None))
    ax3.set_title("Ranking of BE Application", y=-0.15, fontsize=font_size)
    for a, b in zip(x, best):
        ax3.text(b+20 if b < 200 else b-9, a-0.3, '%.1f' % b, ha='center', va='bottom',
                 fontsize=font_size)
    # ax0.xaxis.set_ticks_position('top')
    # ax0.tick_params(direction='in', labelsize=font_size)
    # ax0.set_xlabel('Best-effort Score', fontsize=font_size)
    # ax0.set(xlim=(0.3, 0.8))
    # ax.legend(ncol=3, loc='upper center', bbox_to_anchor=(0.5, 1.21))

    # ax.yaxis.set_major_locator(plt.MultipleLocator(50))
    # ax0.grid(axis='x', color='0.7', linestyle=':')
    ax1.grid(axis='x', color='0.7', linestyle=':')
    ax2.grid(axis='x', color='0.7', linestyle=':')
    ax3.grid(axis='x', color='0.7', linestyle=':')
    fig.tight_layout()

    plt.savefig("121_score.svg")
    plt.show()
