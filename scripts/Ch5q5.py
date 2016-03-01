# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 23:41:24 2016

@author: joe
"""

#Chapter5 Question 5

import numpy as np
from matplotlib import pyplot as plt

x = 15
sigma = 10
x1 = sigma*np.random.randn(10000)+x
x2 = 15
sigma2 = 10
x3=(sigma2*np.random.rand(10000)+x2)
plt.figure(1)
plt.subplot(1,1,1)
plt.hist(x1)
plt.hist(x3)
plt.ylim(0,500)
plt.xlim(-50,50)
plt.xlabel('x')
plt.ylabel('frequency')


#Applying the Gaussian function
x = 15
sigma=10
x4 = sigma*np.random.randn(10000)+x
prob1 = (1/np.sqrt(2*np.pi))*np.exp(-(1/2)*x4**2)
x5 = sigma*np.random.randn(10000)+x
prob2 = (1/np.sqrt(2*np.pi))*np.exp(-(1/2)*x5**2)
plt.figure(2)
plt.subplot(1,1,1)
plt.hist(prob1)
plt.hist(prob2)
plt.xlabel('P(x)')
plt.ylabel('x')
plt.xlim(-0,0.5)





