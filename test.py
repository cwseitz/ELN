from eln.canvas import Canvas
from eln.plots import add_table
from skimage.io import imread
import pandas as pd
import csv

#Read data
im = imread('/home/cwseitz/Desktop/mC2000LP100exp1375Hz_MMStack_Pos0.ome.tif')
meta = pd.read_csv('/home/cwseitz/Desktop/mC1500P100exp2005Hz_meta.csv')

#Plot and save
c = Canvas(title='Test Analysis', nrows=2, ncols=2, figsize=(10,10))
add_table(c.ax[0,0], meta)
c.ax[0,1].imshow(im[0], cmap='gray')
c.save('/home/cwseitz/Desktop/test.pdf')
