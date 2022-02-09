# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 12:06:38 2022

@author: Okan

https://leetcode.com/problems/container-with-most-water/

"""



height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

def maxArea(height):
    
    y = len(height)-1
    x = 0
    maxArea=0
    
    while x<y:
        val=height[y]
        if height[x]<val:
            val=height[x]                
        pixArea=val*abs(x-y)
        if maxArea<pixArea:
            maxArea = pixArea
 
        if height[x] < height[y]:
            x+=1
        else:
            y=y-1
            
            
            
    return maxArea

print(maxArea(height))


