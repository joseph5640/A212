# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 23:36:28 2016

@author: joe
"""
#Chapter 5 Question 1

import numpy as np
import matplotlib.pyplot as plt

np.x = np.linspace(-1,3)
np.y = 3*np.x**2
plt.plot(np.x,np.y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = 3x^2')
plt.show() 

