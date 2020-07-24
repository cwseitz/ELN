import matplotlib.pyplot as plt
from ..plot import add_hist, format_ax
from ..util import add_diff

def plot_dvalue_estimate(df):

	"""
	Estimate the diffusion coefficient of an ensemble of particles
	undergoing 2D brownian motion from the distribution of displacements.
	Useful only when the particles can be assumed to have the same
	diffusion coefficient, as in a simulation.

	For a brownian particle: D = variance/2t

	Parameters
	----------
	"""

	def add_mean(sample, ax):

		mean = r'$\mu$ = %.2E' % sample.mean()
		var = r'$\sigma^{2}$ = %.2E' % sample.var()

		ax.text(.7, .7, mean + ',\n' + var, \
				fontsize=10, transform=ax.transAxes)


	fig, ax = plt.subplots(1, 3, figsize=(10,3))

	df = df[['frame', 'dx', 'dy', 'dr']].groupby('frame').var().reset_index()
	df['dx'] /= 2*df['frame']
	df['dy'] /= 2*df['frame']
	df['dr'] /= 2*df['frame']
	df = df.rename(columns={'dx': 'D_x', 'dy':'D_y', 'dr':'D_r'})

	add_hist(ax[0], df, 'D_x')
	ax[0].set_yticks([])
	format_ax(ax[0], ax_is_box=False, legend_loc='upper right')

	add_hist(ax[1], df, 'D_y')
	ax[1].set_yticks([])
	format_ax(ax[1], ax_is_box=False, legend_loc='upper right')

	add_hist(ax[2], df, 'D_r')
	ax[2].set_yticks([])
	format_ax(ax[2], ax_is_box=False, legend_loc='upper right')
