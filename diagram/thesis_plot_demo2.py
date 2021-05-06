import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.axisartist as axisartist

# https://zhuanlan.zhihu.com/p/89502616

b0 = 1600
b0_line = [b0, b0, b0, b0, b0, b0, b0, b0, b0, b0]
data_r0 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

data_y0 = [b0, b0]; data_y1 = [b0,0];data_y2 = [0, 0];data_y3 = [b0-100, 0];data_y4 = [b0-100, b0-100];data_y5 = [b0-100, 0];data_y6=[0, 0];data_y7=[0, b0];data_y8=[b0, b0];data_y9=[b0, 0];data_y10=[0, b0];data_y11=[b0, b0];data_y12=[0, b0]
data_x0 = [0, 1]; data_x1 = [1, 1];data_x2 = [1, 2];data_x3 = [2, 2];data_x4 = [2, 3];data_x5 = [3, 3];data_x6=[3, 4];data_x7=[4,4];data_x8=[4,4.5];data_x9=[4.5,4.5];data_x10=[5.5,5.5];data_x11=[5.5,6];data_x12=[6,6]

fig = plt.figure(figsize=(6, 5))
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)

ax.plot(data_r0, b0_line, linewidth=0.8, linestyle='-.', color='black')
plt.text(7 - 0.2, b0, '$B_0=1600$', fontsize=10.5)
r = 800
r_line = [r, r, r, r, r, r, r, r, r, r]
data_r = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ax.plot(data_r, r_line, linewidth=0.8, linestyle='-.', color='black')
plt.text(7-0.1, r, '$R=800$', fontsize=10.5)

ax.plot(data_x0, data_y0, linewidth=0.8, color='black')
ax.fill_between(data_x0, 0, data_y0, hatch='//', alpha=0)
ax.plot(data_x1, data_y1, linewidth=0.8, color='black')
ax.fill_between(data_x1, 0, data_y1, hatch='//', alpha=0)
ax.plot(data_x2, data_y2, linewidth=0.8, color='black')
ax.fill_between(data_x2, 0, data_y2, hatch='//', alpha=0)
ax.plot(data_x3, data_y3, linewidth=0.8, color='black')
ax.fill_between(data_x3, 0, data_y3, hatch='//', alpha=0)
ax.plot(data_x4, data_y4, linewidth=0.8, color='black')
ax.fill_between(data_x4, 0, data_y4, hatch='//', alpha=0)
ax.plot(data_x5, data_y5, linewidth=0.8, color='black')
ax.fill_between(data_x5, 0, data_y5, hatch='//', alpha=0)
ax.plot(data_x6, data_y6, linewidth=0.8, color='black')
ax.fill_between(data_x6, 0, data_y6, hatch='//', alpha=0)
ax.plot(data_x7, data_y7, linewidth=0.8, color='black')
ax.fill_between(data_x7, 0, data_y7, hatch='//', alpha=0)
ax.plot(data_x8, data_y8, linewidth=0.8, color='black')
ax.fill_between(data_x8, 0, data_y8, hatch='//', alpha=0)
ax.plot(data_x9, data_y9, linewidth=0.8, color='black')
ax.fill_between(data_x9, 0, data_y9, hatch='//', alpha=0)
ax.plot(data_x10, data_y10, linewidth=0.8, color='black')
ax.fill_between(data_x10, 0, data_y10, hatch='//', alpha=0)
ax.plot(data_x11, data_y11, linewidth=0.8, color='black')
ax.fill_between(data_x11, 0, data_y11, hatch='//', alpha=0)
ax.plot(data_x12, data_y12, linewidth=0.8, color='black')
ax.fill_between(data_x12, 0, data_y12, hatch='//', alpha=0)

helper_line = [b0, 0]; hl_x = [2, 2]
ax.plot(hl_x, helper_line, linewidth=0.8, linestyle='--', color='black')

# ax.axes.xaxis.set_ticks([])
# ax.axes.yaxis.set_ticks([])
ax.axis['right'].set_visible(False)
ax.axis['top'].set_visible(False)

ax.axis["left"].set_axisline_style("->", size=1.0)
ax.axis["bottom"].set_axisline_style("-|>", size=1.0)

ax.axis["left"].set_axis_direction("top")
ax.axis["bottom"].set_axis_direction("bottom")

ax.axis['left'].label.set_text('IOPS')
ax.axis['bottom'].label.set_text('Time')
plt.annotate('$T/2$', xy=(0.5, 0), xytext=(1, -100), arrowprops=dict(arrowstyle='->'))
plt.annotate('$T/2$', xy=(2.5, 0), xytext=(3, -100), arrowprops=dict(arrowstyle='->'))
plt.annotate('$T/4$', xy=(4.25, 0), xytext=(4.75, -100), arrowprops=dict(arrowstyle='->'))
plt.annotate('$T/4$', xy=(5.75, 0), xytext=(6.25, -100), arrowprops=dict(arrowstyle='->'))
ax.set_xticklabels(['', '', '$T_0$', '$T_1$', '$T_2$'])
ax.xaxis.set_major_locator(plt.MultipleLocator(2))
ax.yaxis.set_major_locator(plt.MultipleLocator(500))

ax.set(xlim=(0, 7), ylim=(0, 2000))
plt.grid(color='0.7', linestyle=':')
# plt.savefig("oltp_io_pattern.png")
plt.savefig("burst_schedule_result0.png")
plt.show()
