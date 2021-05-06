import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import math

color_styles = ['#d73027', '#f46d43', '#2c7bb6', '#fdae61', '#fee090', '#ffffbf', '#e0f3f8', '#abd9e9', '#74add1',
                '#4575b4']
markers = ['x', 'o', '>', 'square', '*', '<']
linestyles = ['solid', 'dashed', 'dashdot', 'dotted']
client_labels = ['B, burst=4000', 'R, rserve=1000', 'BE']


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


def stat_resource_time(raw_data, win_size=20):
    rts = []
    i = 0
    while i < len(raw_data):
        s = math.fsum(raw_data[i:i+win_size])
        s = s / 3600.0
        rts.append(s)
        i = i + win_size

    return rts


if __name__ == '__main__':
    plt.rc('font', family='Arial')
    font_size = 16
    labels = ['R Policy', 'B Policy', 'BE Policy']
    # methods = ['', 'Reservation App', 'Burst App', 'Best-effort App', '']
    x = np.arange(len(labels))  # the label locations
    width = 0.2  # the width of the bars
    fig, ax = plt.subplots(1, 3, figsize=(9, 5))
    ax0 = ax[0]
    ax1 = ax[1]
    ax2 = ax[2]

    reserve = [24258.0/1000.0, 27425.0/1000.0, 39498.0/1000.0]
    burst = [62, 66.0, 73.0]
    best = [98.0, 300.0, 300.0]

    # rx = np.array([0])
    ax0.bar(x, reserve, width, color='#93cf93', edgecolor='black')
    ax1.bar(x, burst, width, color='#93cf93', edgecolor='black')
    ax2.bar(x, best, width, color='#93cf93', edgecolor='black')

    ax0.bar([0], [reserve[0]], width, color='r', edgecolor='black')
    ax1.bar([0], [burst[0]], width, color='r', edgecolor='black')
    ax2.bar([0], [best[0]], width, color='r', edgecolor='black')

    ax0.set_ylabel('$95^{th}$ Latency($\mu$s)', fontsize=font_size)
    ax0.set_xlabel('', fontsize=font_size)
    ax0.set_xticks(x)
    ax0.set_xticklabels(labels)
    ax0.set_xticklabels(labels=labels, rotation=30)
    ax0.tick_params(direction='in', labelsize=font_size)
    ax0.set_title("R Application", y=-0.25, fontsize=font_size)

    labels = ['B Policy', 'BE Policy', 'R Policy']
    ax1.set_ylabel('Completion Time(s)', fontsize=font_size)
    ax1.set_xlabel('', fontsize=font_size)
    ax1.set_xticks(x)
    ax1.set_xticklabels(labels)
    ax1.set_xticklabels(labels=labels, rotation=30)
    ax1.tick_params(direction='in', labelsize=font_size)
    ax1.set_title("B Application", y=-0.25, fontsize=font_size)

    labels = ['BE Policy', 'B Policy', 'R Policy']
    ax2.set_ylabel('Completion Time(s)', fontsize=font_size)
    ax2.set_xlabel('', fontsize=font_size)
    ax2.set_xticks(x)
    ax2.set_xticklabels(labels)
    ax2.set_xticklabels(labels=labels, rotation=30)
    ax2.tick_params(direction='in', labelsize=font_size)
    ax2.set_title("BE Application", y=-0.25, fontsize=font_size)

    fig.tight_layout()

    plt.savefig("fairness_r2b.svg")
    plt.show()
