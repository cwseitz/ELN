import matplotlib.pyplot as plt
from bamboo.util import format_ax

fig, ax = plt.subplots()
format_ax(ax, ax_is_box=False)
plt.show()