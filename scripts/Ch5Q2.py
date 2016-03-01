# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 23:47:40 2016

@author: joe
"""
#Chapter 5 Question 2

import numpy as np
import matplotlib.pyplot as plt

np.x = np.linspace(-15,15)
np.y = ((np.cos(x)/((1+(1/5)*np.x**2))))
plt.plot(np.x,np.y, 'c')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
