# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 16:16:01 2022

@author: Okan
"""

nums = [0,1,0,3,12]


def moveZeroes(nums):
    i = 0
    if len(nums) < 2:
        return nums
    while i < len(nums):
        if nums[i] == 0:
            j = i + 1
            while j < len(nums) and nums[j] == 0:
                j += 1
            if j > len(nums) - 1:
                break
            nums[i], nums[j] = nums[j], nums[i]
        i += 1
    return nums


print(moveZeroes(nums))    



      