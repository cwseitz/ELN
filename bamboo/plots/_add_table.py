import matplotlib.pyplot as plt
import pandas as pd

def add_table(ax, df):

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
		x = list(x)[1:] #remove index value
		cell_text.append(x)
	ax.table(cellText=cell_text, loc='bottom')
