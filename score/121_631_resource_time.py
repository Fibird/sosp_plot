import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib import ticker

color_styles = ['#93cf93', '#eb9192', '#f2bae0', '#cccccc']
markers = ['x', 'o', '>', 'square', '*', '<']
linestyles = ['solid', 'dashed', 'dashdot', 'dotted']

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

win_size_121 = 80

def stat_resource_time_121(raw_data):
    rts = []
    i = 0
    while i < len(raw_data):
        s = math.fsum(raw_data[i:i+win_size_121])
        s = s / 3600.0
        rts.append(s)
        i = i + win_size_121

    #rts[0] = (rts[0] + rts[1] + rts[2]) / 3

    return rts

win_size_631 = 20

def stat_resource_time_631(raw_data):
    rts = []
    i = 0
    while i < len(raw_data):
        s = math.fsum(raw_data[i:i+win_size_631])
        s = s / 3600.0
        rts.append(s)
        i = i + win_size_631

    # rts[0] = (rts[0] + rts[1] + rts[2]) / 3

    return rts

def to_percent(temp, position):
    return '%1.0f'%(100*temp) + '%'

font_name = 'Arial'
font_size = 28
plt.rc('font', family='Arial')
font1 = {'family': font_name,
         'weight': 'normal',
         'size': font_size,
         }
fig, axes = plt.subplots(nrows=1, ncols=2, sharey='row', figsize=(17, 8))


# 121
ax121 = axes[1]
standard_values_121 = [5000.0 * win_size_121 * 0.6 / 3600.0, 5000.0 * win_size_121 * 0.3 / 3600.0, 5000.0 * win_size_121 * 0.1 / 3600]
datas_121 = get_data_from_sim("../isolation2/121/r2b_iops.log")
r2b_rts = []
for data in datas_121:
    r2b_rts.append(stat_resource_time_121(data)[0])

datas_121 = get_data_from_sim("../isolation2/121/rwl_iops.log")
rwl_rts = []
for data in datas_121:
    rwl_rts.append(stat_resource_time_121(data)[0])

datas_121 = get_data_from_sim("../isolation2/121/rw_iops.log")
rw_rts = []
for data in datas_121:
    rw_rts.append(stat_resource_time_121(data)[0])

datas_121 = get_data_from_sim("../isolation2/121/rl_iops.log")
rl_rts = []
for data in datas_121:
    rl_rts.append(stat_resource_time_121(data)[0])

datas_121 = get_data_from_sim("../isolation2/121/wl_iops.log")
wl_rts = []
for data in datas_121:
    wl_rts.append(stat_resource_time_121(data)[0])

datas_121 = get_data_from_sim("../isolation2/121/r_iops.log")
r_rts = []
for data in datas_121:
    r_rts.append(stat_resource_time_121(data)[0])

datas_121 = get_data_from_sim("../isolation2/121/w_iops.log")
w_rts = []
for data in datas_121:
    w_rts.append(stat_resource_time_121(data)[0])

datas_121 = get_data_from_sim("../isolation2/121/l_iops.log")
l_rts = []
for data in datas_121:
    l_rts.append(stat_resource_time_121(data)[0])

methods = ['Target', 'R2B', 'R+W', 'W+L', 'R+W+L', 'L', 'R+L', 'R', 'W']
labels = ["Burst application's", "Reservation application's", "Best-effort application's", "Unused"]
ind = np.arange(len(methods))
# plt.xticks(ind, methods)
ax121.set_xticks(ind)
ax121.set_xticklabels(methods, fontsize=font_size, rotation=30)
# plt.xticks(rotation=30)

# plt.ylabel('Scores')
# plt.yticks(np.arange(0, 81, 20))

r2b_sum = np.sum(r2b_rts[3])
rl_sum = np.sum(rl_rts[3])
rw_sum = np.sum(rw_rts[3])
rwl_sum = np.sum(rwl_rts[3])
wl_sum = np.sum(wl_rts[3])
r_sum = np.sum(r_rts[3])
w_sum = np.sum(w_rts[3])
l_sum = np.sum(l_rts[3])
target_ratio = [0.25, 0.5, 0.25]

total_rt = 5100.0 * win_size_121 / 3600

Bottom = (target_ratio[0], r2b_rts[0] / total_rt, rw_rts[0] / total_rt, wl_rts[0] / total_rt, rwl_rts[0] / total_rt, l_rts[0] / total_rt, rl_rts[0] / total_rt, r_rts[0] / total_rt, w_rts[0] / total_rt)
Center = (target_ratio[1], r2b_rts[1] / total_rt, rw_rts[1] / total_rt, wl_rts[1] / total_rt, rwl_rts[1] / total_rt, l_rts[1] / total_rt, rl_rts[1] / total_rt, r_rts[1] / total_rt, w_rts[1] / total_rt)
Top = (target_ratio[2], r2b_rts[2] / total_rt, rw_rts[2] / total_rt, wl_rts[2] / total_rt, rwl_rts[2] / total_rt, l_rts[2] / total_rt, rl_rts[2] / total_rt, r_rts[2] / total_rt, w_rts[2] / total_rt)
Other = 1 - np.array(Top) - np.array(Bottom) - np.array(Center)

for a, b in zip(ind, Bottom):
    ax121.text(a, b / 2 - 0.03, '%.1f' % (b * 100), ha='center', va='bottom', fontsize=font_size)
for a, b in zip(ind, Center):
    ax121.text(a, (Center[a] + Bottom[a] * 2) / 2 - 0.03, '%.1f' % (b * 100), ha='center', va='bottom', fontsize=font_size)
for a, b in zip(ind, Top):
    ax121.text(a, (1 - Other[a] + Bottom[a] + Center[a]) / 2 - 0.03, '%.1f' % (b * 100), ha='center', va='bottom', fontsize=font_size)
for a, b in zip(ind, Other):
    ax121.text(a, (1 + Top[a] + Bottom[a] + Center[a]) / 2 - 0.03, '%.1f' % (b * 100), ha='center', va='bottom', fontsize=font_size)

d = []
for i in range(0, len(Bottom)):
    sum = Bottom[i] + Center[i]
    d.append(sum)

width = 0.73
p1 = ax121.bar(ind, Bottom, width, color=color_styles[0])
p2 = ax121.bar(ind, Center, width, bottom=Bottom, color=color_styles[1])
p3 = ax121.bar(ind, Top, width, bottom=d, color=color_styles[2])
d = np.array(Bottom) + np.array(Top) + np.array(Center)
p4 = ax121.bar(ind, Other, width, bottom=d, color=color_styles[3])

plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(to_percent))
ax121.axhline(0.75, linestyle=':', color='k')
ax121.axhline(0.25, linestyle=':', color='k')
ax121.locator_params(axis='y', nbins=6)
ax121.tick_params(direction='in', labelsize=font_size)
ax121.set_title("2:1:1's Resource Time Distribution", y=-0.21, fontsize=font_size)
plt.xticks(rotation=30)

plt.ylim((0, 1))


# 631
ax631 = axes[0]
standard_values_631 = [5000.0 * win_size_631 * 0.6 / 3600.0, 5000.0 * win_size_631 * 0.3 / 3600.0, 5000.0 * win_size_631 * 0.1 / 3600]
datas = get_data_from_sim("../isolation2/631/r2b_iops.log")
r2b_rts = []
for data in datas:
    r2b_rts.append(stat_resource_time_631(data)[0])

datas = get_data_from_sim("../isolation2/631/rwl_iops.log")
rwl_rts = []
for data in datas:
    rwl_rts.append(stat_resource_time_631(data)[0])

datas = get_data_from_sim("../isolation2/631/rw_iops.log")
rw_rts = []
for data in datas:
    rw_rts.append(stat_resource_time_631(data)[0])

datas = get_data_from_sim("../isolation2/631/rl2_iops.log")
rl_rts = []
for data in datas:
    rl_rts.append(stat_resource_time_631(data)[0])

datas = get_data_from_sim("../isolation2/631/wl_iops.log")
wl_rts = []
for data in datas:
    wl_rts.append(stat_resource_time_631(data)[0])

datas = get_data_from_sim("../isolation2/631/r2_iops.log")
r_rts = []
for data in datas:
    r_rts.append(stat_resource_time_631(data)[0])

datas = get_data_from_sim("../isolation2/631/w_iops.log")
w_rts = []
for data in datas:
    w_rts.append(stat_resource_time_631(data)[0])

datas = get_data_from_sim("../isolation2/631/l_iops.log")
l_rts = []
for data in datas:
    l_rts.append(stat_resource_time_631(data)[0])

methods = ['Target', 'R2B', 'R+L', 'R+W', 'R+W+L', 'W+L', 'R', 'W', 'L']
labels = ["Burst", "Reservation", "Best-effort", "Unused"]
ind = np.arange(len(methods))
# plt.xticks(ind, methods)
ax631.set_xticks(ind)
ax631.set_xticklabels(methods, fontsize=font_size, rotation=30)

# plt.ylabel('Scores')
# plt.yticks(np.arange(0, 81, 20))

r2b_sum = np.sum(r2b_rts[3])
rl_sum = np.sum(rl_rts[3])
rw_sum = np.sum(rw_rts[3])
rwl_sum = np.sum(rwl_rts[3])
wl_sum = np.sum(wl_rts[3])
r_sum = np.sum(r_rts[3])
w_sum = np.sum(w_rts[3])
l_sum = np.sum(l_rts[3])
target_ratio = [0.6, 0.3, 0.1]
total_rt = 5100.0 * win_size_631 / 3600

Bottom = (target_ratio[0], r2b_rts[0] / total_rt, rw_rts[0] / total_rt, wl_rts[0] / total_rt, rwl_rts[0] / total_rt, l_rts[0] / total_rt, rl_rts[0] / total_rt, r_rts[0] / total_rt, w_rts[0] / total_rt)
Center = (target_ratio[1], r2b_rts[1] / total_rt, rw_rts[1] / total_rt, wl_rts[1] / total_rt, rwl_rts[1] / total_rt, l_rts[1] / total_rt, rl_rts[1] / total_rt, r_rts[1] / total_rt, w_rts[1] / total_rt)
Top = (target_ratio[2], r2b_rts[2] / total_rt, rw_rts[2] / total_rt, wl_rts[2] / total_rt, rwl_rts[2] / total_rt, l_rts[2] / total_rt, rl_rts[2] / total_rt, r_rts[2] / total_rt, w_rts[2] / total_rt)
Other = 1 - np.array(Top) - np.array(Bottom) - np.array(Center)

for a, b in zip(ind, Bottom):
    ax631.text(a, b / 2 - 0.03, '%.1f' % (b * 100), ha='center', va='bottom', fontsize=font_size)
for a, b in zip(ind, Center):
    ax631.text(a, (Center[a] + Bottom[a] * 2) / 2 - 0.03, '%.1f' % (b * 100), ha='center', va='bottom', fontsize=font_size)
for a, b in zip(ind, Top):
    ax631.text(a, (1 - Other[a] + Bottom[a] + Center[a]) / 2 - 0.03, '%.1f' % (b * 100), ha='center', va='bottom', fontsize=font_size)
for a, b in zip(ind, Other):
    ax631.text(a, (1 + Top[a] + Bottom[a] + Center[a]) / 2 - 0.03, '%.1f' % (b * 100), ha='center', va='bottom', fontsize=font_size)

d = []
for i in range(0, len(Bottom)):
    sum = Bottom[i] + Center[i]
    d.append(sum)

width = 0.73
p1 = ax631.bar(ind, Bottom, width, color=color_styles[0])
p2 = ax631.bar(ind, Center, width, bottom=Bottom, color=color_styles[1])
p3 = ax631.bar(ind, Top, width, bottom=d, color=color_styles[2])
d = np.array(Bottom) + np.array(Top) + np.array(Center)
p4 = ax631.bar(ind, Other, width, bottom=d, color=color_styles[3])

plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(to_percent))
ax631.axhline(0.9, linestyle=':', color='k')
ax631.axhline(0.6, linestyle=':', color='k')
ax631.locator_params(axis='y', nbins=6)
ax631.tick_params(direction='in', labelsize=font_size)
ax631.set_title("3:6:1's Resource Time Distribution", y=-0.21, fontsize=font_size)

plt.ylim((0, 1))

# handles, labels = ax631.get_legend_handles_labels()


# plt.subplots_adjust(top=0.002, bottom=0.001)
# fig.legend((p1[0], p2[0], p3[0], p4[0]), labels, ncol=2, loc="center left",  prop=font1, bbox_to_anchor=(0.1, 0.5), framealpha=0.4)

plt.tight_layout()

plt.savefig("resource_time_121_631.svg")

plt.show()
