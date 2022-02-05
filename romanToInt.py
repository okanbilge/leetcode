# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 17:14:58 2022

@author: Okan
"""

s="MCMXCIV"
def romanToInt(s):
    dictLetters={}
    dictLetters["I"]=1
    dictLetters["V"]=5
    dictLetters["X"]=10
    dictLetters["L"]=50
    dictLetters["C"]=100
    dictLetters["D"]=500
    dictLetters["M"]=1000
    
    
    total=0
    index=0
    while len(s)>index:
        
        if index+1<len(s):
            if (s[index]=="I" and s[index+1]=="V") or (s[index]=="I" and s[index+1]=="X"):
                total+= (dictLetters[s[index+1]]-1)
                index+=2
    
            elif (s[index]=="X" and s[index+1]=="L") or (s[index]=="X" and s[index+1]=="C"):
                total+= (dictLetters[s[index+1]]-10)
                index+=2
            elif (s[index]=="C" and s[index+1]=="D") or (s[index]=="C" and s[index+1]=="M"):
                total+= (dictLetters[s[index+1]]-100)
                index+=2
            else:
                total+=dictLetters[s[index]]
                index+=1
        else:
            total+=dictLetters[s[index]]
            index+=1
    
    return total

print(romanToInt(s))
    
    
    