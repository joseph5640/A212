# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 13:34:25 2016

@author: joe
"""

import numpy as np
from matplotlib import pyplot as plt

def sum(n):
        y = np.sum(n)
        return y 
n =[]
for n in range(0,n):
    n.append(np.random.random_integers(6)) 
return np.sum(n)
    
y=[]
for n in range (0,10000):
    y.append(np.sum(2))

y=[]
for n in range (0,1000):
    y.append(np.sum(3))

plt.subplot(1,1,1) 
plt.hist(y, bins=11)




