import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib import ticker

color_styles = ['#93cf93', '#eb9192', '#f2bae0', '#cccccc']
markers = ['x', 'o', '>', 'square', '*', '<']
linestyles = ['solid', 'dashed', 'dashdot', 'dotted']

font_name = 'Arial'
font_size = 22
plt.rc('font', family='Arial')
font1 = {'family': font_name,
         'weight': 'normal',
         'size': font_size,
         }
fig, ax = plt.subplots(figsize=(10, 1.2))


labels = ["Burst application's", "Reservation application's", "Best-effort application's", "Unused"]
ind = np.arange(3)

Bottom = (0, 0, 0)
Center = (0, 0, 0)
Top = (0, 0, 0)
Other = 1 - np.array(Top) - np.array(Bottom) - np.array(Center)

width = 0.73
p1 = plt.bar(ind, Bottom, width, color=color_styles[0])
p2 = plt.bar(ind, Center, width, color=color_styles[1])
p3 = plt.bar(ind, Top, width, color=color_styles[2])
p4 = plt.bar(ind, Other, width, color=color_styles[3])

plt.bar(ind, Bottom, width+0.2, color='white', edgecolor='white')
plt.bar(ind, Center, width+0.2, color='white', edgecolor='white')
plt.bar(ind, Top, width+0.2, color='white', edgecolor='white')
plt.bar(ind, Other, width+0.2, color='white', edgecolor='white')

plt.axis('off')

fig.legend((p1[0], p2[0], p3[0], p4[0]), labels, ncol=2, loc="center",  prop=font1, bbox_to_anchor=(0.52, 0.5), edgecolor='black')

plt.tight_layout()

plt.savefig("resource_time_legend.svg")

plt.show()
