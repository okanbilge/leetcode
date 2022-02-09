# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 12:06:38 2022

@author: Okan

https://leetcode.com/problems/container-with-most-water/

"""


height = [1,0,0,0,0,0,0,2,2]

def maxArea(height):
    
    areaList={}
    for x in range(len(height)):
        areaList[x]=0
        
    if len(height)==2:
        if height[0]<height[1]:
            areaList[0]=height[0]
        else:
            areaList[0]=height[1]

    else:
        
        for x in range(len(height)-1):
            for y in range(x+1,len(height)):
                multiplicator = y-x
                if height[x]<height[y] :
                    if areaList[x]<height[x]*multiplicator:
                        areaList[x]=height[x]*multiplicator
                else:
                    if areaList[x]<height[y]*multiplicator:
                        areaList[x]=height[y]*multiplicator

         
        
    return max(areaList.values())

print(maxArea(height))