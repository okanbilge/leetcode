# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 20:27:09 2022

@author: Okan
"""

nums = [-1,0,3,5,9,12,33,44,55,66,77,88,99,100,110,120,130]
target = 123



def search(nums, target):
    arrayShape=len(nums)
    midPoint=arrayShape//2
    
    if arrayShape==1:
        if nums[0]==target:
            return 1
        else:
            return -1
    print("Nums Midpoint " , nums[midPoint])
    if nums[midPoint]>target:
        smallIndex=search(nums[:midPoint],target)
        if smallIndex>0:
            return smallIndex
        else:
             return -1
        
    elif nums[midPoint]<target:
        smallIndex=search(nums[midPoint:],target)
        if smallIndex>0:
            return midPoint+smallIndex
        else:
             return -1
    else:
        return midPoint

    
    
print(search(nums, target))       
        