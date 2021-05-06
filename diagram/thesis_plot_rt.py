import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.axisartist as axisartist

# https://zhuanlan.zhihu.com/p/89502616

def get_data_from_iostat(file_name, disk="rbd0"):
    data = []
    f = open(file_name)
    for line in f:
        line_list = line.split()
        if line_list and line_list[0] == disk and len(line_list) > 6:
            r = line_list[5]
            w = line_list[6]
            data.append((float(r) + float(w)) / 4)

    f.close()
    return data


def make_sparse(arr, stride):
    sparse_arr = []
    count = 0
    for a in arr:
        count = count + 1
        if count >= stride:
            sparse_arr.append(a)
            count = 0
    return sparse_arr


def remove_singular(arr, value):
    for index in range(len(arr)):
        if arr[index] >= value:
            arr[index] = np.mean(arr[index-10:index+10])

    return arr

font_name = 'Arial'
font_size = 22
plt.rc('font', family='Arial')
font1 = {'family': font_name,
         'weight': 'normal',
         'size': font_size,
         }

## data
# data_list = get_data_from_log("ceph_perf_log_4m16s1t.log")
#data_list0 = get_data_from_iostat("result/oltp-result-2.log")
data_list0 = get_data_from_iostat("../result/cgroup_test-0326094801.log", "rbd2")

#ddata_list0 = data_list0[150:500]
ddata_list0 = data_list0[552:560]
dx0 = np.arange(0, len(ddata_list0), 1)

fig = plt.figure(figsize=(6, 5))
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)

ax.plot(dx0, ddata_list0, linewidth=0.8, color='black', label="oltp: (2000)")
ax.fill_between(dx0, 0, ddata_list0, hatch='//', alpha=0)

ax.axes.xaxis.set_ticks([])
ax.axes.yaxis.set_ticks([])
ax.axis['right'].set_visible(False)
ax.axis['top'].set_visible(False)
#ax.axis["x"] = ax.new_floating_axis(0, 0)
ax.axis["left"].set_axisline_style("->", size=1.0)

#ax.axis["y"] = ax.new_floating_axis(1, 0)
ax.axis["bottom"].set_axisline_style("-|>", size=1.0)

ax.axis["left"].set_axis_direction("top")
ax.axis["bottom"].set_axis_direction("right")


ax.axis['left'].label.set_text('Throughput')
ax.axis['bottom'].label.set_text('Time')
ax.axis['left'].label.set_font(font1)
ax.axis['bottom'].label.set_font(font1)

# ax.xaxis.set_major_locator(plt.MultipleLocator(500))
#ax.set(xlim=(0, len(dx0) - 1), ylim=(0, None))
ax.set(xlim=(0, len(dx0) - 1), ylim=(0, 10000))
plt.text(3.5, 3000, 'S', fontsize=font_size, style='italic')
#plt.grid(color='0.7', linestyle=':')
# plt.savefig("oltp_io_pattern.png")
plt.savefig("rt_demo.svg")
plt.show()
