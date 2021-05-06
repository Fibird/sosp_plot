import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.axisartist as axisartist

# https://zhuanlan.zhihu.com/p/89502616

r0 = 500
r = 800
r0_line = [r0, r0, r0, r0, r0, r0, r0, r0, r0, r0]
data_r0 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
r_line = [r, r, r, r, r, r, r, r, r, r]
data_r = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

data_y0 = [r0, r0]; data_y1 = [r0, (r - r0) * 2 + r0];data_y2 = [(r - r0) * 2 + r0, (r - r0) * 2 + r0];data_y3 = [(r - r0) * 2 + r0, r];data_y4 = [r, r, r];data_y5 = [r, r0-100];data_y6=[r0-100, r0-100];data_y7=[r0-100,(r - r0) * 2 + r0];data_y8=[(r - r0) * 2 + r0,(r - r0) * 2 + r0];data_y9=[(r - r0) * 2 + r0,r0];data_y10=[r0, r0];
data_x0 = [0, 1]; data_x1 = [1, 1];data_x2 = [1, 2];data_x3 = [2, 2];data_x4 = [2, 3, 4];data_x5 = [4, 4];data_x6=[4, 5];data_x7=[5,5];data_x8=[5,6];data_x9=[6,6];data_x10=[6,7]

fig = plt.figure(figsize=(6, 5))
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)

ax.plot(data_r0, r0_line, linewidth=0.8, linestyle='-.', color='black')
plt.text(7-0.2, r0, '$R_0=500$', fontsize=10.5)
ax.plot(data_r, r_line, linewidth=0.8, linestyle='-.', color='black')
plt.text(7-0.2, r, '$R=800$', fontsize=10.5)


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

helper_line = [r, 0]; hl_x = [2,2]
ax.plot(hl_x, helper_line, linewidth=0.8, linestyle='--', color='black')
helper_line = [r0, 0]; hl_x = [4,4]
ax.plot(hl_x, helper_line, linewidth=0.8, linestyle='--', color='black')
helper_line = [r0, 0]; hl_x = [6,6]
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
ax.set_xticklabels(['', '', '$T_0$', '$T_1$', '$T_2$'])
ax.xaxis.set_major_locator(plt.MultipleLocator(2))
ax.yaxis.set_major_locator(plt.MultipleLocator(500))

ax.set(xlim=(0, 7), ylim=(0, r * 2))
plt.text(3.5, 3000, 'S', fontsize=14, style='italic')
plt.grid(color='0.7', linestyle=':')
# plt.savefig("oltp_io_pattern.png")
plt.savefig("reserv_schedule_result0.png")
plt.show()
