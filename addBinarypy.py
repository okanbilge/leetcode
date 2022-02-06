# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 13:50:32 2022

@author: Okan
"""



a = "11"
b = "1"

def addBinary(a,b):
    
    dummy = 0
    index1=1
    c=""
    while index1<=len(a) and index1<=len(b):
        if int(b[-index1])+int(a[-index1])+dummy>2:
            c="1"+c
            index1+=1
            dummy=1
        elif int(b[-index1])+int(a[-index1])+dummy>1:
            c="0"+c
            index1+=1
            dummy = 1    
        elif int(b[-index1])+int(a[-index1])+dummy==1:
            c="1"+c
            index1+=1
            dummy = 0
        else:
            c="0"+c
            index1+=1
            dummy = 0
            
    if len(a)>len(b):
        while index1<=len(a):
            if int(a[-index1])+dummy>1:
                c="0"+c
                index1+=1
                dummy=1

            elif int(a[-index1])+dummy==1:
                c="1"+c
                index1+=1
                dummy = 0
            else:
                c="0"+c
                index1+=1
                dummy = 0
    if len(b)>len(a):
        while index1<=len(b):
            if int(b[-index1])+dummy>1:
                c="0"+c
                index1+=1
                dummy=1

            elif int(b[-index1])+dummy==1:
                c="1"+c
                index1+=1
                dummy = 0
            else:
                c="0"+c
                index1+=1
     
    if dummy==1:
        c="1"+c
        
    
    return c 
        
    
print(addBinary(a,b))