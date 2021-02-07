import matplotlib.pyplot as plt
import pandas as pd

def add_table(ax, df, hide_ax=True):

	"""
	Add a DataFrame as a table to the axis

	Parameters
	----------
	ax : object
		matplotlib axis.
	"""

	cell_text = [];
	for row in range(len(df)):
		x = df.iloc[row]
		cell_text.append(list(x))
	ax.table(cellText=cell_text, loc='best')

	if hide_ax:
		ax.spines['top'].set_visible(False)
		ax.spines['bottom'].set_visible(False)
		ax.spines['left'].set_visible(False)
		ax.spines['right'].set_visible(False)
