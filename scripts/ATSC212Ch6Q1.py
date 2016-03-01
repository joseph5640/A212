# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 21:35:30 2016

@author: joe
"""
#Chapter 6

#Question 1 (a)
s=6
while s>6:
    i=s*(s+1)
    S=s*(s-1)*(s-2)*(s-3)*(s-4)*(s-5)
    print("factorial=S")
    

#Question 1 (b)

for s in range(7,12):
    if s>=6:  S=s*(s-1)*(s-2)*(s-3)*(s-4)*(s-5)
    print("factorial sequence for s>6 with s(s+1) = {0:0.1f}".format(S))
for s in range(1,6):
    if s<6: 
        i=s*(s+1)
    S *=i
    print("factorial sequence for s<6 with s(s+1) = {0:0.1f}".format(S))

    
        
        
        
        
        
        
            

        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    



