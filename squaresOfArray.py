# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 09:57:36 2022

@author: Okan
"""


nums=[55,44,-4,0,8,10,5,11]

def sortedSquares(nums):

    
    n = len(nums)
            
    for x in range(n):
        isArraySorted = True
        
        
        for y in range(n - x - 1):
            print(nums)

            if nums[y] > nums[y + 1]:
                
                nums[y], nums[y + 1] = nums[y + 1], nums[y]
                isArraySorted = False

          
        if isArraySorted:
            break
        
        
    return nums


print(sortedSquares(nums))
