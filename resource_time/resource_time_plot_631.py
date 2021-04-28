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
win_size = 20

def stat_resource_time(raw_data):
    rts = []
    i = 0
    while i < len(raw_data):
        s = math.fsum(raw_data[i:i+win_size])
        s = s / 3600.0
        rts.append(s)
        i = i + win_size

    return rts


def io_plot(plot_data, save_img=False):
    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111)
    xs = np.arange(0, len(plot_data[0]), 1)
    count = 0
    for ys in plot_data:
        ys = stat_resource_time(ys)
        print(ys)
        xs = np.arange(0, len(ys), 1)
        if count < (len(plot_data) - 1):
            ax.plot(xs, ys, linewidth=2, color=color_styles[count], linestyle=linestyles[count], marker=markers[count],
                    label=client_labels[count])
        count = count + 1

    # ax.xaxis.set_major_locator(plt.MultipleLocator(50))
    # ax.yaxis.set_major_locator(plt.MultipleLocator(10))
    ax.set(xlim=(0, len(xs) - 1), ylim=(0, None))
    # ax.legend(loc='center right')

    font1 = {'family': 'Times New Roman',
             'weight': 'normal',
             'size': 16,
             }
    ncol = int(math.ceil(6 / 2.))
    plt.legend(ncol=ncol, loc='upper center', prop=font1)
    plt.grid(axis='y', color='0.7', linestyle=':')
    plt.tick_params(labelsize=16)
    labels = ax.get_xticklabels() + ax.get_yticklabels()
    [label.set_fontname('Times New Roman') for label in labels]
    ax.set_xlabel("Time (sec)", font1)
    ax.set_ylabel("IOPS", font1)

    if save_img:
        date_str = datetime.now().strftime("%y%m%d%H%M%S")
        plt.savefig("sim_plot" + str(date_str) + ".svg")
    plt.show()


if __name__ == '__main__':
    plt.rc('font', family='Arial')

    standard_values = [5000.0 * win_size * 0.6 / 3600.0, 5000.0 * win_size * 0.3 / 3600.0, 5000.0 * win_size * 0.1 / 3600]
    datas = get_data_from_sim("../iops/r2b_631_long_iops.log")
    r2b_rts = []
    for data in datas:
        r2b_rts.append(stat_resource_time(data)[0])

    datas = get_data_from_sim("../iops/rwl_631_long_iops.log")
    rwl_rts = []
    for data in datas:
        rwl_rts.append(stat_resource_time(data)[0])

    datas = get_data_from_sim("../iops/rw_631_long_iops.log")
    rw_rts = []
    for data in datas:
        rw_rts.append(stat_resource_time(data)[0])

    datas = get_data_from_sim("../iops/rl_631_long_iops.log")
    rl_rts = []
    for data in datas:
        rl_rts.append(stat_resource_time(data)[0])

    datas = get_data_from_sim("../iops/wl_631_long_iops.log")
    wl_rts = []
    for data in datas:
        wl_rts.append(stat_resource_time(data)[0])

    datas = get_data_from_sim("../iops/r_631_long_iops.log")
    r_rts = []
    for data in datas:
        r_rts.append(stat_resource_time(data)[0])

    datas = get_data_from_sim("../iops/w_631_long_iops.log")
    w_rts = []
    for data in datas:
        w_rts.append(stat_resource_time(data)[0])

    datas = get_data_from_sim("../iops/l_631_long_iops.log")
    l_rts = []
    for data in datas:
        l_rts.append(stat_resource_time(data)[0])

    labels = ['Burst application', 'Reservation application', 'Best-effort application']
    methods = ['R2B', 'R+L', 'R+W', 'R+W+L', 'W+L', 'R', 'W', 'L']
    x = np.arange(len(methods))  # the label locations
    burst_line = np.full(len(methods), standard_values[0])
    reserve_line = np.full(len(methods), standard_values[1])
    best_line = np.full(len(methods), standard_values[2])
    width = 0.2  # the width of the bars
    blx = x - width
    rlx = x
    belx = x + width
    fig, ax = plt.subplots()

    burst = [r2b_rts[0], rl_rts[0], rw_rts[0], rwl_rts[0], wl_rts[0], r_rts[0], w_rts[0], l_rts[0]]
    reserve = [r2b_rts[1], rl_rts[1], rw_rts[1], rwl_rts[1], wl_rts[1], r_rts[1], w_rts[1], l_rts[1]]
    best = [r2b_rts[2], rl_rts[2], rw_rts[2], rwl_rts[2], wl_rts[2], r_rts[2], w_rts[2], l_rts[2]]

    rects1 = ax.bar(x - width, burst, width, color='#93cf93', hatch='//', edgecolor='black', label=labels[0])
    rects2 = ax.bar(x, reserve, width, color='#eb9192', hatch='oo', edgecolor='black', label=labels[1])
    rects3 = ax.bar(x + width, best, width, color='#f2bae0', hatch='--', edgecolor='black',  label=labels[2])
    ax.plot(blx, burst_line, color='black', linestyle='--', label="burst target line")
    ax.plot(rlx, reserve_line, color='black', linestyle=':', label="reservation target line")
    ax.plot(belx, best_line, color='black', linestyle='-', label="best-effort target line")

    ax.set_ylabel('Resource Time($Bw\cdot h$)', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(methods)
    ax.legend(ncol=3, loc='upper center', bbox_to_anchor=(0.5, 1.21))

    # ax.yaxis.set_major_locator(plt.MultipleLocator(50))
    plt.grid(axis="y")
    fig.tight_layout()

    plt.savefig("resource_time_stats_631-1.svg")
    plt.show()
