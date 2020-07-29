import numpy as np
import matplotlib.pyplot as plt

from matplotlib.figure import Figure
from datetime import datetime

class Canvas:

	"""

	A object that wraps matplotlib.pyplot.subplots() to create a
	canvas-like figure object for output as 8.5 x 11 pdf.

	"""

	def __init__(self, template=None, nrows=1, ncols=1, title='', author='',
				 left=None, right=None, bottom=None, top=None, wspace=None, hspace=None,
				 figsize=(8.5,11)):

		"""

		Parameters
		----------
		template : list, optional
		 list of params for matplotlib.axes.Axes.inset_axes
		nrows: int, optional
		 Number of rows if not using a custom template
		ncols: int, optional
		 Number of columns if not using a custom template
		title: str, optional
		 Title of the document
		author: str, optional
		 Author of the document
		right: float, optional
		 The position of the right edge of the subplots, as a fraction of the figure width.
		left: float, optional
		 The position of the left edge of the subplots, as a fraction of the figure width.
		top : float, optional
		 The position of the top edge of the subplots, as a fraction of the figure height.
		bottom : float, optional
		 The position of the bottom edge of the subplots, as a fraction of the figure height.
		wspace : float, optional
		 The width of the padding between subplots, as a fraction of the average axes width.
		hspace : float, optional
		 The height of the padding between subplots, as a fraction of the average axes height.
		figsize: tuple, optional
		 The size of the figure. Defaults to (8.5, 11) standard letter

		"""

		self.title=title; self.author=author; self.template=template;

		if template:
			self.get_custom(figsize)
			self.hide_canvas_ax()

		else:
			self.fig, self.ax = plt.subplots(nrows,ncols,figsize=figsize,
											 edgecolor='red',linewidth=10)
			self.fig.subplots_adjust(right=right,bottom=bottom,
									 left=left, top=top,
									 wspace=wspace,hspace=hspace)
		self.add_header()

	def get_custom(self, figsize):

		self.fig, self.canvas_ax = plt.subplots(1,1,figsize=figsize,
										 edgecolor='red',linewidth=10)
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
