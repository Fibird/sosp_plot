import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib import ticker

color_styles = ['#93cf93', '#eb9192', '#f2bae0', '#33a02c']
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
win_size = 80

def stat_resource_time(raw_data):
    rts = []
    i = 0
    while i < len(raw_data):
        s = math.fsum(raw_data[i:i+win_size])
        s = s / 3600.0
        rts.append(s)
        i = i + win_size

    #rts[0] = (rts[0] + rts[1] + rts[2]) / 3

    return rts


def to_percent(temp, position):
    return '%1.0f'%(100*temp) + '%'

font_name = 'Arial'
font_size = 20
plt.rc('font', family='Arial')
font1 = {'family': font_name,
         'weight': 'normal',
         'size': font_size,
         }
fig, ax = plt.subplots(figsize=(8, 5))

standard_values = [5000.0 * win_size * 0.6 / 3600.0, 5000.0 * win_size * 0.3 / 3600.0, 5000.0 * win_size * 0.1 / 3600]
datas = get_data_from_sim("../isolation2/121/r2b_iops.log")
r2b_rts = []
for data in datas:
    r2b_rts.append(stat_resource_time(data)[0])

datas = get_data_from_sim("../isolation2/121/rwl_iops.log")
rwl_rts = []
for data in datas:
    rwl_rts.append(stat_resource_time(data)[0])

datas = get_data_from_sim("../isolation2/121/rw_iops.log")
rw_rts = []
for data in datas:
    rw_rts.append(stat_resource_time(data)[0])

datas = get_data_from_sim("../isolation2/121/rl_iops.log")
rl_rts = []
for data in datas:
    rl_rts.append(stat_resource_time(data)[0])

datas = get_data_from_sim("../isolation2/121/wl_iops.log")
wl_rts = []
for data in datas:
    wl_rts.append(stat_resource_time(data)[0])

datas = get_data_from_sim("../isolation2/121/r_iops.log")
r_rts = []
for data in datas:
    r_rts.append(stat_resource_time(data)[0])

datas = get_data_from_sim("../isolation2/121/w_iops.log")
w_rts = []
for data in datas:
    w_rts.append(stat_resource_time(data)[0])

datas = get_data_from_sim("../isolation2/121/l_iops.log")
l_rts = []
for data in datas:
    l_rts.append(stat_resource_time(data)[0])

methods = ['Target', 'R2B', 'R+W', 'W+L', 'R+W+L', 'L', 'R+L', 'R', 'W']
labels = ["Burst application's", "Reservation application's", "Best-effort application's", "Unused"]
ind = np.arange(len(methods))
plt.xticks(ind, methods)

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

total_rt = 5100.0 * win_size / 3600

Bottom = (target_ratio[0], r2b_rts[0] / total_rt, rw_rts[0] / total_rt, wl_rts[0] / total_rt, rwl_rts[0] / total_rt, l_rts[0] / total_rt, rl_rts[0] / total_rt, r_rts[0] / total_rt, w_rts[0] / total_rt)
Center = (target_ratio[1], r2b_rts[1] / total_rt, rw_rts[1] / total_rt, wl_rts[1] / total_rt, rwl_rts[1] / total_rt, l_rts[1] / total_rt, rl_rts[1] / total_rt, r_rts[1] / total_rt, w_rts[1] / total_rt)
Top = (target_ratio[2], r2b_rts[2] / total_rt, rw_rts[2] / total_rt, wl_rts[2] / total_rt, rwl_rts[2] / total_rt, l_rts[2] / total_rt, rl_rts[2] / total_rt, r_rts[2] / total_rt, w_rts[2] / total_rt)
Other = 1 - np.array(Top) - np.array(Bottom) - np.array(Center)

for a, b in zip(ind, Bottom):
    plt.text(a, b / 2 - 0.03, '%.1f' % (b * 100), ha='center', va='bottom', fontsize=font_size)
for a, b in zip(ind, Center):
    plt.text(a, (Center[a] + Bottom[a] * 2) / 2 - 0.03, '%.1f' % (b * 100), ha='center', va='bottom', fontsize=font_size)
for a, b in zip(ind, Top):
    plt.text(a, (1 - Other[a] + Bottom[a] + Center[a]) / 2 - 0.03, '%.1f' % (b * 100), ha='center', va='bottom', fontsize=font_size)
for a, b in zip(ind, Other):
    plt.text(a, (1 + Top[a] + Bottom[a] + Center[a]) / 2 - 0.03, '%.1f' % (b * 100), ha='center', va='bottom', fontsize=font_size)

d = []
for i in range(0, len(Bottom)):
    sum = Bottom[i] + Center[i]
    d.append(sum)

width = 0.73
p1 = plt.bar(ind, Bottom, width, color=color_styles[0])
p2 = plt.bar(ind, Center, width, bottom=Bottom, color=color_styles[1])
p3 = plt.bar(ind, Top, width, bottom=d, color=color_styles[2])
d = np.array(Bottom) + np.array(Top) + np.array(Center)
p4 = plt.bar(ind, Other, width, bottom=d, color=color_styles[3])

plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(to_percent))
plt.axhline(0.75, linestyle=':', color='k')
plt.axhline(0.25, linestyle=':', color='k')
ax.locator_params(axis='y', nbins=6)
ax.tick_params(direction='in', labelsize=font_size)
plt.xticks(rotation=30)

plt.ylim((0, 1))
# plt.legend((p1[0], p2[0], p3[0], p4[0]), labels, ncol=2, loc='center', bbox_to_anchor=(0.5, 0.65))
plt.tight_layout()

plt.savefig("resource_time_121.svg")

plt.show()
