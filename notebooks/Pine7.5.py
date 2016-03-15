# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 11:52:55 2016

@author: joe
"""

#Pine's Exercise 7.5
import numpy as np
from matplotlib import pyplot as plt

t,v,dy = np.loadtxt("/Users/joe/Desktop/Velocityvstimedataforafallingmass.txt", skiprows=2, unpack=True)
print(t)
print(v)
print(dy)

def LineFit(x, y):
    
    xavg = x.mean()
    slope = (y*(x-xavg)).sum()/(x*(x-xavg)).sum()
    yint = y.mean()-slope*xavg
    return slope, yint

def LineFitWt(x, y, dy):
    dy2 = dy**2.
    denom= np.sum(1/(dy**2.))
    xnumerator = np.sum(x/dy2)
    ynumerator = np.sum(y/dy2)
    xhat = xnumerator/denom
    yhat = ynumerator/denom
    bnum = np.sum((x - xhat)*y/dy2)
    bdenom = np.sum((x - xhat)*x/dy2)
    slope = bnum/bdenom
    yint = yhat - slope*xhat
    sigma_b_squared = 1/(bdenom)
    a = sigma_b_squared
    sigma_a_squared = (a**2)*xhat*(np.sum(x)/(denom))
    return slope,yint,sigma_a_squared

x = np.array([t])
y = np.array([v])
dy = np.array([dy])
plt.plot(LineFit(x,y))
plt.errorbar(x,y,yerr=dy,fmt='o')

dy2 = dy**2.
denom= np.sum(1/(dy**2.))
xnumerator = np.sum(x/dy2)
ynumerator = np.sum(y/dy2)
xhat = xnumerator/denom
yhat = ynumerator/denom
bnum = np.sum((x - xhat)*y/dy2)
bdenom = np.sum((x - xhat)*x/dy2)
slope = bnum/bdenom
yint = yhat - slope*xhat
sigma_b_squared = 1/(bdenom)
a = sigma_b_squared
sigma_a_squared = (a**2)*xhat*(np.sum(x)/(denom))

plt.figure(2)
plt.plot(a,sigma_a_squared)






    
    



    
    
    
    
    
    




