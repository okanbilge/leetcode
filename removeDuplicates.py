# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 23:07:37 2022

@author: Okan
"""
nums = [0,0,1,1,1,1,2,3,3]

def removeDuplicates(nums):
    
    allNumber=len(nums)
    number=0
    while number< allNumber-2:
        
        if nums[number]==nums[number+1] and nums[number]==nums[number+2]:
            nums[number+1:]=nums[number+2:]
            allNumber-=1
        else:
            number+=1
    return len(nums)
    
removeDuplicates(nums)   
    
    
    
    