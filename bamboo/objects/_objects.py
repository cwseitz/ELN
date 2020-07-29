import numpy as np
import matplotlib.pyplot as plt

from matplotlib.figure import Figure
from datetime import datetime

class Canvas(Figure):

    """

    A object that wraps matplotlib.pyplot.subplots() to create a
    'canvas' like object that be written to PDF.

    Plots can be added. A template can be chosen, or the bound_arr
    can be specified for custom applications

    Example 1
    -------------
    >>>from bamboo.templates import *
    >>>from bamboo.objects import Canvas
    >>>author = 'Clayton Seitz'
    >>>title = 'Title'
    >>>template = get_template_1()
    >>>canvas = Canvas(template=template, author=author, title=title)

    Example 2
    -------------
    >>>from bamboo.templates import *
    >>>from bamboo.objects import Canvas
    >>>author = 'Clayton Seitz'
    >>>title = 'Title'
    >>>canvas = Canvas(template=template, nrows=2, ncols=2,
                        right=0.75, bottom=0.5, wspace=0.75, hspace=0.75,
                        author=author, title=title)


    """

    def __init__(self, template=None, nrows=1, ncols=1, title='', author='',
                 right=0.5, bottom=0.5, wspace=None, hspace=None,
                 figsize=(8.5,11)):

        super(Figure, self).__init__()

        self.title=title; self.author=author; self.template=template;

        if template:
            self.get_custom(figsize)
            self.hide_canvas_ax()

        else:
            self.fig, self.ax = plt.subplots(nrows,ncols,figsize=figsize,
                                             edgecolor='gray',linewidth=8)
            self.fig.subplots_adjust(right=right,bottom=bottom,
                                     wspace=wspace,hspace=hspace)
        self.add_header()

    def get_custom(self, figsize):

        self.fig, self.canvas_ax = plt.subplots(1,1,figsize=figsize,
                                         edgecolor='gray',linewidth=8)
        self.ax = [self.canvas_ax.inset_axes(bound) for bound in self.template]

    def preview(self):

        self.hide_sub_ax_ticks()
        plt.show()

    def hide_sub_ax_ticks(self):
        for ax in np.array(self.ax).flatten():
            ax.set_xticks([]); ax.set_yticks([])

    def hide_canvas_ax(self):

        self.canvas_ax.set_xticks([]); self.canvas_ax.set_yticks([])
        self.canvas_ax.spines['right'].set_visible(False)
        self.canvas_ax.spines['top'].set_visible(False)
        self.canvas_ax.spines['left'].set_visible(False)
        self.canvas_ax.spines['bottom'].set_visible(False)

    def add_header(self):

        text = self.title
        text += datetime.today().strftime('\n%Y-%m-%d-%H:%M:%S')
        text += '\n' + self.author

        self.fig.suptitle(text, x=0.1, y=0.975,
                          horizontalalignment='left', fontsize=10)
