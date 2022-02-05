# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 17:14:58 2022

@author: Okan
"""

s="MCDLXXVI"

def romanToInt(s):
    dictLetters={}
    dictLetters["I"]=1
    dictLetters["V"]=5
    dictLetters["X"]=10
    dictLetters["L"]=50
    dictLetters["C"]=100
    dictLetters["D"]=500
    dictLetters["M"]=1000

    dictLetters["Q"]=4
    dictLetters["T"]=9
    dictLetters["K"]=40
    dictLetters["P"]=90
    dictLetters["F"]=400
    dictLetters["R"]=900
    
    s=s.replace("IV", "Q")    
    s=s.replace("IX", "T")    
    s=s.replace("XL", "K")    
    s=s.replace("XC", "P")    
    s=s.replace("CD", "F")    
    s=s.replace("CM", "R")    
    
    total = 0
    for x in range (len(s)):
        total+=dictLetters[s[x]]


    return total

print(romanToInt(s))
    
    
    