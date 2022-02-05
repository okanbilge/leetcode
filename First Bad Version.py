# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 21:09:27 2022

@author: Okan
"""



def isBadVersion(n):
    if n>0:
        return True
    else:
        return False
    

class Solution:
    def firstBadVersion(self, n: int) -> int:
        midPoint=n//2
        falseCounter=midPoint//2
        while True:    
            if isBadVersion(midPoint):
                if not(isBadVersion(midPoint)) and isBadVersion(midPoint+1) :
                    midPoint+=1
                    break
                midPoint-=falseCounter

            else:
                if not(isBadVersion(midPoint)) and isBadVersion(midPoint+1):
                    midPoint+=1
                    break
                midPoint+=falseCounter
                
            if falseCounter>0:
                falseCounter=falseCounter//2
            else:
                falseCounter=1
        return midPoint


    