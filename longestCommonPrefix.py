# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 17:58:52 2022

@author: Okan
"""
strs = ["ab", "a"]
def longestCommonPrefix(strs):
    
    letterList=""
    strComp = strs[0]
    minLetter=len(strs[0])
    for x in range(1,len(strs)):
        if len(strs[x])<minLetter:
            minLetter=len(strs[x]) 
    
    for y in range (minLetter):
        for x in range(1,len(strs)):
            if strComp[y]!=strs[x][y]:
                print( "letterList")
        letterList+=strComp[y]
        
    return letterList



print(longestCommonPrefix(strs))    
    
    
    
    
    
    
    
    
    
    
    