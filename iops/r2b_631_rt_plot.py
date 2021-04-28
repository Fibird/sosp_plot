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
    datas = get_data_from_sim("sim_r2b_631_iops.log")
    r2b_rts = []
    for data in datas:
        r2b_rts.append(stat_resource_time(data)[0])

    datas = get_data_from_sim("sim_rwl_631_iops.log")
    rwl_rts = []
    for data in datas:
        rwl_rts.append(stat_resource_time(data)[0])

    labels = ['Burst application', 'Reservation application', 'Best-effort application']
    methods = ['R2B', 'R+W+L', 'R+W', 'W+L', 'R', 'W', 'L']
    x = np.arange(len(methods))  # the label locations
    width = 0.2  # the width of the bars
    fig, ax = plt.subplots()

    burst = [r2b_rts[0], rwl_rts[0], 0, 0, 0, 0, 0]
    reserve = [r2b_rts[1], rwl_rts[1], 0, 0, 0, 0, 0]
    best = [r2b_rts[2], rwl_rts[2], 0, 0, 0, 0, 0]

    rects1 = ax.bar(x - width, burst, width, color='#93cf93', hatch='//', edgecolor='black', label=labels[0])
    rects2 = ax.bar(x, reserve, width, color='#eb9192', hatch='oo', edgecolor='black', label=labels[1])
    rects3 = ax.bar(x + width, best, width, color='#f2bae0', hatch='--', edgecolor='black',  label=labels[2])

    ax.set_ylabel('Resource Time($Bw\cdot h$)', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(methods)
    ax.legend()

    # ax.yaxis.set_major_locator(plt.MultipleLocator(50))
    plt.grid(axis="y")
    # fig.tight_layout()

    plt.savefig("resource_time_stats.svg")
    plt.show()
