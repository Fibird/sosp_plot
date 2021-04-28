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
    win_size = 20
    utils = []
    total_perf = 5000 * 20
    datas = get_data_from_sim("../iops/r2b_631_long_iops.log")
    total_perf0 = datas[3][:win_size]
    utils.append(np.sum(np.array(total_perf0)) / total_perf)

    datas = get_data_from_sim("../iops/rwl_631_long_iops.log")
    total_perf1 = datas[3][:win_size]
    utils.append(np.sum(np.array(total_perf1)) / total_perf)

    datas = get_data_from_sim("../iops/rw_631_long_iops.log")
    total_perf2 = datas[3][:win_size]
    utils.append(np.sum(np.array(total_perf2)) / total_perf)

    datas = get_data_from_sim("../iops/rl_631_long_iops.log")
    total_perf3 = datas[3][:win_size]
    utils.append(np.sum(np.array(total_perf3)) / total_perf)

    datas = get_data_from_sim("../iops/wl_631_long_iops.log")
    total_perf4 = datas[3][:win_size]
    utils.append(np.sum(np.array(total_perf4)) / total_perf)

    datas = get_data_from_sim("../iops/r_631_long_iops.log")
    total_perf5 = datas[3][:win_size]
    utils.append(np.sum(np.array(total_perf5)) / total_perf)

    datas = get_data_from_sim("../iops/w_631_long_iops.log")
    total_perf6 = datas[3][:win_size]
    utils.append(np.sum(np.array(total_perf6)) / total_perf)

    datas = get_data_from_sim("../iops/l_631_long_iops.log")
    total_perf7 = datas[3][:win_size]
    utils.append(np.sum(np.array(total_perf7)) / total_perf)

    labels = ['Burst application', 'Reservation application', 'Best-effort application']
    methods = ['R2B', 'R+L', 'R+W', 'R+W+L', 'W+L', 'R', 'W', 'L']
    x = np.arange(len(methods))  # the label locations
    width = 0.6  # the width of the bars
    fig, ax = plt.subplots()

    rects1 = ax.bar(x, utils, width, color='#93cf93', edgecolor='black')
    for a, b in zip(x, utils):
        plt.text(a - 0.27, b + 0.1, '%.2f' % b, ha='center', va='bottom', fontsize=14)

    ax.set_ylabel('System Utilization', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(methods)
    # ax.legend(ncol=3, loc='upper center', bbox_to_anchor=(0.5, 1.21))

    # ax.yaxis.set_major_locator(plt.MultipleLocator(50))
    plt.grid(axis="y")
    fig.tight_layout()

    plt.savefig("average_utils.svg")
    plt.show()
