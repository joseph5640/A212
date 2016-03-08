# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 23:59:39 2016

@author: joe
"""
#Chapter 7 Question 1

import numpy as np
from matplotlib import pyplot as plt

np.x=np.linspace(0,20)

def j(x):
    np.y1 = []
    for xx in x:
        if  xx ==0:
            np.y1+=[1]
    else: np.y1=np.sin(np.xx)/np.xx
    return np.array(np.y1)

np.y1= np.sin(np.x)/np.x
plt.plot(np.x,np.y1)

def j2(x):
    np.y2 = []
    for xx in x:
        if xx==0:
            np.y2+=[1]
    else: np.y2= (np.sin(np.xx)/(np.xx**2)) - (np.cos(np.xx)/np.xx)
    return np.array(np.y2)




def j3(x):
    np.y3 = []
    for xx in x:
        if xx==0:
            np.y3+=[1]
    else: np.y3 = (3/(np.xx**2))*((np.sin(np.xx)/np.xx)-(np.cos(np.xx)/np.xx**2))
    return np.array(np.y3)


 


        






