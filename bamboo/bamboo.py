import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from datetime import datetime

class Figure(Figure):

    def __init__(self, bound_arr, figsize):

        super(Figure, self).__init__()

        self.fig, self.ax = plt.subplots(1,1, figsize=figsize)
        self.grid = [self.ax.inset_axes(bound) for bound in bound_arr]
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['left'].set_visible(False)
        self.ax.spines['bottom'].set_visible(False)
        self.ax.set_xticks([]); self.ax.set_yticks([])

class Rectangle_Template(Figure):

    def __init__(self, nrows, ncols, figsize=(8.5,11), title=None, author=None):


        tmp = np.ones((9,))
        widths = (1/(1.15*3))*tmp; heights = (1/(1.5*3))*tmp

        x_arr = np.linspace(0.0, 0.7, 3)
        y_arr = np.linspace(0.2, 0.8, 3)
        xv,yv = np.meshgrid(x_arr,y_arr)

        self.bound_arr = np.stack((np.ravel(xv),
                                   np.ravel(yv),
                                   widths, heights),
                                   axis=-1)

        self.bound_arr = np.flip(self.bound_arr, axis=0)
        self.bound_arr = self.bound_arr[0:3*nrows]
        self.bound_arr = np.flip(self.bound_arr, axis=0)
        Figure.__init__(self, self.bound_arr, figsize)
        self.add_header()


    def add_header(self):

        text = title
        text += datetime.today().strftime('\n%Y-%m-%d-%H:%M:%S')
        text += '\n' + author

        self.ax.text(0.0, 1.05, text,
                verticalalignment='bottom', horizontalalignment='left',
                transform=self.ax.transAxes,
                color='black', fontsize=10)
