# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 11:06:10 2022

@author: Okan
"""


haystack = "a" 
needle = "a"


def strStr(haystack,needle):
    counter=0
    if needle=="":
        return 0
    else:
        for x in range(len(haystack)-len(needle)+1):
            if haystack[x:x+len(needle)]==needle:
                counter=x
    if counter>0:
        return counter
    else:
        return -1
    
    
print( strStr(haystack,needle))


