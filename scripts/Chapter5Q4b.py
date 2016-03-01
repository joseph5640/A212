# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 01:23:37 2016

@author: joe
"""
#Chapter 5 Question 4(b)

import numpy as np
from matplotlib import pyplot as plt

t = [10,4.5,8.0,11.5,15.0,18.5,22.0,25.5,29.0,32.5,36.0,39.5,43]
d = [2.94,8.29,9.36,11.6,9.32,7.75,8.06,5.60,4.50,4.01,2.62,1.70,2.03]
dy = [0.7,1.2,1.2,1.4,1.3,1.1,1.2,1.0,0.8,0.8,0.7,0.6,0.6]

np.t = np.linspace(0,50)
np.d = (3+(1/2)*np.sin((np.pi*np.t)/5))*np.t*np.exp(-np.t/10)
plt.plot(np.t,np.d, 'b-', label ='theory')

plt.subplot(1,1,1)
plt.plot(t,d, 'o',label='data')
plt.legend(loc = 'upper right')
plt.errorbar(t,d,fmt ='ro', yerr=dy,ecolor="black" )
plt.xlabel('time(s)')
plt.ylabel('position (cm)') 

















