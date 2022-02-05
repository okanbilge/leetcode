# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 22:08:34 2022

@author: Okan
"""


nums = [1,3,5,6,33,55,66,77]

target = 2



def searchInsert(nums, target):
    arrayShape=len(nums)
    midPoint=arrayShape//2    

    if arrayShape==1:
        if nums[0]<target:
           return +1
        else:
            return 0
        
    if nums[midPoint]>target:
        if nums[midPoint-1]<target:
            return midPoint+1
        return searchInsert(nums[:midPoint],target)

    else:
        return midPoint+searchInsert(nums[midPoint:],target)

    return midPoint

  
    
    
    
    
    
    
print(searchInsert(nums, target))       
        