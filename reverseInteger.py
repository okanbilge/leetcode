# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 17:02:01 2022

@author: Okan
"""

x = 1534236469


def reverse(x):
    
    if x>0:
        sign=1
    elif x<0:
        sign=0
        x=x*-1
    else:
        return 0

    newX=""

    while x>0:
        newX+=str(x%10)
        x=x//10
    

    x=int(newX)
    if abs(x)>(2**31)-1 :
        return 0 
    
    
    if sign==0:
        return -1*x
    return x
    
    
    
    
    
print(reverse(x))