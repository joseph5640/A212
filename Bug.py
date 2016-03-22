# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:06:19 2016

@author: joe
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from pathlib import Path
import a212data
datadir = a212data.__path__[0]
stinkpath = Path(datadir).joinpath('stinkbug.png')
img=mpimg.imread(str(stinkpath))
imgplot = plt.imshow(img)
lum_img = img[:,:,0]
imgplot = plt.imshow(lum_img)
imgplot.set_cmap('hot')
plt.show()

import seaborn as sns
imgplot=plt.imshow(img)
lum_ing=img[:,:,0]
imgplot=plt.imshow(lum_ing)
pal =sns.light_palette((250,100,50),input='husl', as_cmap=True)
imgplot.set_cmap(pal)
plt.show(imgplot.set_cmap(pal))

import seaborn as sns
imgplot=plt.imshow(img)
lum_ing=img[:,:,0]
imgplot=plt.imshow(lum_ing)
pal =sns.dark_palette((260,80,60),input='husl', as_cmap=True)
imgplot.set_cmap(pal)
plt.show(imgplot.set_cmap(pal))

import seaborn as sns
imgplot=plt.imshow(img)
lum_ing=img[:,:,0]
imgplot=plt.imshow(lum_ing)
pal =sns.cubehelix_palette(start=4, rot=-2, as_cmap=True)
imgplot.set_cmap(pal)
plt.show(imgplot.set_cmap(pal))












