from eln.canvas import Canvas
from eln.plots import add_table
from skimage.io import imread, imsave
from skimage.measure import regionprops
import scipy.optimize as op
import matplotlib.pyplot as plt
import numpy as np

def exponential(x, a, k, b):
    return a*np.exp(x*k) + b

#Read data

path = '/Users/cwseitz/Desktop/'
im = imread(path + 'mC2000LP100exp1375Hz_MMStack_Pos0.ome.tif')
mask = imread(path + 'mC2000LP100exp1375Hz_MMStack_Pos0.ome_mask.tif')

#Fit exponential function to average intensity over the cell body

avg_intensity = []
for i in range(len(im)):
    props = regionprops(mask, intensity_image=im[i])
    avg_intensity.append(props[0].mean_intensity)

avg_intensity = np.array(avg_intensity)
t = np.linspace(0, 30, len(avg_intensity))

popt, pcov = op.curve_fit(exponential, t, avg_intensity, p0=[130,-0.5, 0])

plt.plot(t, avg_intensity)
plt.plot(t, exponential(t, *popt))
plt.xlabel('Time (s)')
plt.ylabel('Intensity (a.u.)')
plt.show()

#Plot and save
# c = Canvas(title='Test Analysis', nrows=2, ncols=2, figsize=(10,10))
# add_table(c.ax[0,0], meta)
# c.ax[0,1].imshow(im[0], cmap='gray')
# c.save('/home/cwseitz/Desktop/test.pdf')
