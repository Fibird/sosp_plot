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

    standard_values = [5000.0 * 20.0 * 0.6 / 3600.0, 5000.0 * 20.0 * 0.3 / 3600.0, 5000.0 * 20.0 * 0.1 / 3600]
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

    labels = ['Reservation policy', 'Burst policy', 'Best-effort policy']
    methods = ['', 'Reservation App', 'Burst App', 'Best-effort App', '']
    x = np.arange(len(methods))  # the label locations
    burst_line = np.full(len(methods), standard_values[0])
    reserve_line = np.full(len(methods), standard_values[1])
    best_line = np.full(len(methods), standard_values[2])
    width = 0.2  # the width of the bars
    fig, ax = plt.subplots()
    ax2 = ax.twinx()

    reserve = [24258.0, 27425.0, 39498.0]; rx = [1 - width, 1, 1+width]
    burst = [73.0, 62, 66.0]; bx = [2 - width, 2, 2+width]
    best = [98.0, 98.0, 98.0]; bex = [3 - width, 3, 3+width]

    rg1 = [24258.0]; rg1x = [1 - width]
    rg2 = [27425]; rg2x = [1]
    rg3 = [39498]; rg3x = [1+width]
    rects1 = ax.bar(rg1x, rg1, width, color='#93cf93', hatch='//', edgecolor='black', label=labels[0])
    rects1 = ax.bar(rg2x, rg2, width, color='#eb9192', hatch='oo', edgecolor='black', label=labels[1])
    rects1 = ax.bar(rg3x, rg3, width, color='#f2bae0', hatch='--', edgecolor='black', label=labels[2])

    g1 = [73, 98.0]; g1x = [2, 3]
    g2 = [62, 98.0]; g2x = [2-width, 3+width]
    g3 = [66.0, 98.0]; g3x = [2+width, 3-width]

    rects1 = ax2.bar(g1x, g1, width, color='#93cf93', hatch='//', edgecolor='black', label=labels[0])
    rects2 = ax2.bar(g2x, g2, width, color='#eb9192', hatch='oo', edgecolor='black', label=labels[1])
    rects3 = ax2.bar(g3x, g3, width, color='#f2bae0', hatch='--', edgecolor='black', label=labels[2])
    ax.set_ylabel('$95^{th}$ Latency($\mu$s)', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(methods)
    ax2.set_ylabel('Complete Time(s)', fontsize=14)
    # ax2.set_xticks(x)

    ax.legend(ncol=3, loc='upper center', bbox_to_anchor=(0.5, 1.15))

    # ax.yaxis.set_major_locator(plt.MultipleLocator(50))
    plt.grid(axis="y")
    fig.tight_layout()

    plt.savefig("envy_free_r2b.svg")
    plt.show()
