# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 17:29:13 2022

@author: Okan
"""

s="-2147483648"

def myAtoi(s):
    
    s=s.lstrip()
    
    if s=="" or s=="-" or s=="+":
        return 0
    

    sign=1
    if s[0]=="-":
        sign=-1        
        s=s[1:]
    elif s[0]=="+":
        s=s[1:]
    
    index=0
    newInt=""
    while s[index].isnumeric() :
        newInt+=s[index]
        if index < len(s)-1:
            index+=1
        else:
            break

    if newInt=="":
        return 0
    x=int(newInt)
    if sign*x < (-1*(2**31)) :
        return -1*(2**31)
    if sign*x>(2**31)-1 :
        return (2**31)-1
    else:
        return sign*x

print(myAtoi(s))






    
    
    