import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.axisartist as axisartist
import matplotlib.patches as mpatches
# https://zhuanlan.zhihu.com/p/89502616

font_name = 'Arial'
font_size = 24
plt.rc('font', family='Arial')
font1 = {'family': font_name,
         'weight': 'normal',
         'size': font_size,
         }

r0 = 500
r = 800
r0_line = [r0, r0, r0, r0, r0, r0, r0, r0, r0, r0]
data_r0 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

b0 = 2000
data_y0 = [b0, b0]; data_y1 = [b0, 0]
data_x0 = [0, 0.5]; data_x1 = [0.5, 0.5]
b1 = 4000
data_y2 = [0, b1];data_y3 = [b1, b1]; data_y4 = [b1, 0]
data_x2 = [0.4, 0.4]; data_x3 = [0.4, 0.65];data_x4 = [0.65, 0.65]

fig = plt.figure(figsize=(6, 5))
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)

# ax.plot(data_r0, r0_line, linewidth=0.8, linestyle=':', color='black')
# plt.text(7+0.1, r0, '$R_0$', fontsize=10.5)


ax.plot(data_x0, data_y0, linewidth=0.8, color='black')
ax.fill_between(data_x0, 0, data_y0, hatch='//', alpha=0)
ax.plot(data_x1, data_y1, linewidth=0.8, color='black')
ax.fill_between(data_x1, 0, data_y1, hatch='//', alpha=0)

ax.plot(data_x2, data_y2, linewidth=0.8, color='black')
ax.fill_between(data_x2, 0, data_y2, hatch='.', alpha=0)
ax.plot(data_x3, data_y3, linewidth=0.8, color='black')
ax.fill_between(data_x3, 0, data_y3, hatch='.', alpha=0)
ax.plot(data_x4, data_y4, linewidth=0.8, color='black')
ax.fill_between(data_x4, 0, data_y4, hatch='.', alpha=0)

ax.axis['right'].set_visible(False)
ax.axis['top'].set_visible(False)

ax.axis["left"].set_axisline_style("->", size=1.0)
ax.axis["bottom"].set_axisline_style("-|>", size=1.0)

ax.axis["left"].set_axis_direction("top")
ax.axis["bottom"].set_axis_direction("bottom")

ax.axis['left'].label.set_text('Throughput')
# ax.axis['bottom'].label.set_text('Time')
ax.axis['left'].label.set_font(font1)
ax.axis['bottom'].label.set_font(font1)
ax.axis['bottom'].major_ticklabels.set_size(font_size)
ax.axis['left'].major_ticklabels.set_size(font_size)
# ax.axis['bottom'].major_ticklabels.set_x(['0', '$0.5T_0$', '$T_0$'])
# # ax.axis['bottom'].major_ticks.set_xdata([0, 1, 2.0])
ax.set_xticks([0, 0.5, 1, 2, 3])
ax.set_xticklabels(['0', '$0.5T_0$', '$T_0$', '$T_1$', '$T_2$'])
ax.xaxis.set_major_locator(plt.MultipleLocator(1))
#ax.yaxis.set_major_locator(plt.MultipleLocator(500))
patches = [mpatches.Patch(hatch="//", label='c0:($B_0=2000,w=1$)', fill=False), mpatches.Patch(hatch=".", label='c1:($B_0=4000,w=1$)', fill=False)]
ax.legend(handles=patches, prop=font1, ncol=1, loc='upper right')

ax.set(xlim=(0, 1), ylim=(0, 5000))
#plt.text(3.5, 3000, 'S', fontsize=14, style='italic')
plt.grid(color='0.7', linestyle=':')
# plt.savefig("oltp_io_pattern.png")

fig.tight_layout()
plt.subplots_adjust(left=0.12)
plt.savefig("burst_conflict_a.svg")
plt.show()
