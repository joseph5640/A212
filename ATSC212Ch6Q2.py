# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 12:06:25 2016

@author: joe
"""
#Chapter 6 Question 2(a)

i= 2
n=100
while (n % i) != 0:
    i += 1

print("The smallest factor of n is =", i) 
#When executed in iPython Shell, I got no output, I just got the string. I
#modified the code to get an output. This loop always terminates, because 
#I set an upper bound of 100 and one cannot divide through zero, thus, the 
#loop terminates as a result. 

#Chapter 6 Question 2(b)
for m in range(3,101):
  if m%m == 1:
      print('prime number')
else:
    print('not a prime number')

for m in range(3,101):
    while (n%i) !=0:
        i+=1 
        print("The smallest factor of n is =", i)
    



