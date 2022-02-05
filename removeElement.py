# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 23:26:29 2022

@author: Okan
"""



nums = [4,5]

val= 4

def removeElement(nums, val):
    counter=0
    for x in range(len(nums)):
        for y in range(len(nums)-1,x,-1):
            if nums[x]==val or nums[x]=="_":
                if nums[x]==val:
                    counter+=1
                nums[x]="_"
            if nums[y]!=val and nums[y]!="_":
                dummy=nums[y]
                nums[y]=nums[x]
                nums[x]=dummy
                break
            else:
                break
    if counter>0:
        nums=nums[:-counter]            
    return len(nums) 
    
    
print( removeElement(nums, val)   )
    
    
    
    