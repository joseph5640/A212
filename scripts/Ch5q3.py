# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 20:33:55 2016

@author: joe
"""
#Chapter 5
#Question 3

import numpy as np
from matplotlib import pyplot as plt
import math

np.x1 = np.linspace(-15,15,200)
np.y1 = np.sin(np.x1)
np.x2 = np.linspace(-15,15,200)
np.y2 = np.cos(np.x2)

plt.figure()
plt.subplot(1,1,1)
plt.plot(np.x1,np.y1, 'g', label="sin(x)" )
plt.plot(np.x2,np.y2, 'k', label = "cos(x)")
plt.xlim(-math.pi,math.pi)
plt.ylim(-1,1)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc= "upper left")
plt.show()










