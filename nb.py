from eln.canvas import Canvas
from eln.plots import add_table
from skimage.io import imread, imsave
from skimage.measure import regionprops
import scipy.optimize as op
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def exp_decay(x,a,b,c):

	return a*(np.exp(-(x-b)/c))

def fit_expdecay(x,y):

	"""Exponential decay fitting function
	Parameters
	----------
	x: 1d ndarray
		raw x data
	y: 1d ndarray
		raw y data
	Returns
	-------
	popt, pcov: 1d ndarray
		optimal parameters and covariance matrix
	"""

	popt, pcov = op.curve_fit(exp_decay, x, y)

	return popt, pcov

#Read data
im = imread('/home/cwseitz/Desktop/mC2000LP100exp1375Hz_MMStack_Pos0.ome.tif')
mask = imread('/home/cwseitz/Desktop/mC2000LP100exp1375Hz_MMStack_Pos0.ome_mask.tif')
meta = pd.read_csv('/home/cwseitz/Desktop/mC1500P100exp2005Hz_meta.csv')

#Fit exponential function to average intensity over the cell body
avg_intensity = []
for i in range(len(im)):
    props = regionprops(mask, intensity_image=im[i])
    avg_intensity.append(props[0].mean_intensity)
avg_intensity = np.array(avg_intensity)
t = np.linspace(0, 1, len(avg_intensity))
popt, pcov = fit_expdecay(t, avg_intensity); print(popt)
plt.plot(t, avg_intensity)
plt.plot(t, exp_decay(t, *popt))
plt.show()

# #Plot and save
# c = Canvas(title='Test Analysis', nrows=2, ncols=2, figsize=(10,10))
# add_table(c.ax[0,0], meta)
# c.ax[0,1].imshow(im[0], cmap='gray')
# c.save('/home/cwseitz/Desktop/test.pdf')
