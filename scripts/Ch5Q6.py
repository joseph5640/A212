# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 12:14:03 2016

@author: joe
"""
#Chapter 5 Question 6

import numpy as np
from matplotlib import pyplot as plt

d = np.array([0.38,0.64,0.91,1.26,1.41,1.66,1.90,2.18])
f = np.array([1.4,1.65,3.0,3.95,4.3,5.20,6.85,7.4])
df = np.array([0.4,0.5,0.4,0.5,0.6,0.5,0.5,0.4])

plt.errorbar(d,f, yerr=df,fmt = 'Dy', ecolor="red", label = 'data')
plt.xlabel('position(cm)')
plt.ylabel('force(N)')
plt.legend(loc ='upper left')
print(np.polyfit(d,f,1)) #regression line
np.x=np.linspace(0,3)
np.y=3.5094*np.x-0.3171 
plt.plot(np.x,np.y, 'k')
plt.xlim(0,2.5)
plt.ylim(0,9)








