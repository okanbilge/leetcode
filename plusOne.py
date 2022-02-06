# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 13:50:32 2022

@author: Okan
"""



digits = [1,9]

def plusOne(digits):
    
    arrayLenght=len(digits)
    index=1
    while arrayLenght-index>-1:
        if digits[-index]==9:

            if arrayLenght==index:
                digits.append(0)
                digits[-index-1]=1
                index+=1
            else:
                digits[-index]=0
                index+=1
            
        
        else:
            digits[-index]+=1            
            return digits
    return digits   

print(plusOne(digits))