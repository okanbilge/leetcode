# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 19:17:48 2022

@author: Okan
"""
s = "(])"

def isValid(s):

    newList=[]
    for x in range (len(s)):

        if  s[x]==")" or s[x]=="]" or s[x]=="}":

            if newList==[]:
                return False
            if (newList[-1]=="(" and s[x]==")") or (newList[-1]=="[" and s[x]=="]") or (newList[-1]=="{" and s[x]=="}"):
                newList.pop()
            else:
                newList.append(s[x])
        else:
            newList.append(s[x])
            
    if newList==[]:
        return True
    else:
        return False   
    
    
    
print(isValid(s))            
            
            
            
            
            
            
            
            
            
            