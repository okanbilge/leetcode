# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 16:46:29 2022

@author: Okan
"""

x=12112312312

def isPalindrome(i):
    
    if i<0:
        return False
    digitList=[]
    dummyInt=i
    while i>0:
        digitList.append(i%10)
        i=i//10
    
    for x in range ((len(digitList)//2)):
        if not (digitList[x]==digitList[-(x+1)]):
            return False
        
    return True   
    

print(isPalindrome(i))








