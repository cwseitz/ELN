import matplotlib.pyplot as plt
from ..plot import add_hist, format_ax
from ..util import add_diff

def plot_trajectory_stats(df):

	"""
	Show acceleration, velocity and position statistics

	Parameters
	----------
	"""

	def add_mean(sample, ax):

		mean = r'$\mu$ = %.2E' % sample.mean()
		var = r'$\sigma^{2}$ = %.2E' % sample.var()

		ax.text(.7, .7, mean + ',\n' + var, \
				fontsize=10, transform=ax.transAxes)

	#
	#~~~~~~~Check if differential columns exist~~~~~~~~~~
	#

	if 'dx' not in df.columns:
		df = add_diff(df, col='x')
	if 'dy' not in df.columns:
		df = add_diff(df, col='y')

	if 'ddx' not in df.columns:
		df = add_diff(df, col='dx')
	if 'ddy' not in df.columns:
		df = add_diff(df, col='dy')


	fig, ax = plt.subplots(2, 2, figsize=(8,7))

	#
	#~~~~~~~Show the velocity distributions~~~~~~~~~~
	#

	add_hist(ax[0,0], df, 'ddx', bins=20)
	ax[0,0].set_yticks([])
	format_ax(ax[0,0], ax_is_box=False)
	add_mean(df['ddx'], ax[0,0])

	add_hist(ax[0,1], df, 'ddy', bins=20)
	ax[0,1].set_yticks([])
	format_ax(ax[0,1], ax_is_box=False)
	add_mean(df['ddy'], ax[0,1])

	# """
	# ~~~~~~~Show the displacement distributions~~~~~~~~~~
	# """

	add_hist(ax[1,0], df, 'dx', bins=20)
	ax[1,0].set_yticks([])
	format_ax(ax[1,0], ax_is_box=False)
	add_mean(df['dx'], ax[1,0])

	add_hist(ax[1,1], df, 'dy', bins=20)
	ax[1,1].set_yticks([])
	format_ax(ax[1,1], ax_is_box=False)
	add_mean(df['dy'], ax[1,1])
