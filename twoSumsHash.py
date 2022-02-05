# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 22:57:10 2022

@author: Okan
"""

nums=[3,2,3,4,6,9]
target=8

def twoSum(nums):
    seen = {}
    for i, value in enumerate(nums):

        remaining = target - nums[i]
            
        if remaining in seen:
            return [i, seen[remaining]]
         
        seen[value] = i 
        
        
twoSum(nums)