# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 16:35:41 2022

@author: Okan
"""


matrix = matrix = [[3,7,8],[9,11,13],[15,16,17]]
def luckyNumbers(matrix):
    
    minListRow= [9999999]*len(matrix)
    bigListCol= [0]*len(matrix[0])
    
    
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] < minListRow[x]:
                minListRow[x]=matrix[x][y]
            if matrix[x][y] > bigListCol[y]:
                bigListCol[y]=matrix[x][y]
    
    for k in range (len(minListRow)):
        if minListRow[k] in bigListCol:
            return minListRow[k]
    
    
    
    
    
    
    
    
print(luckyNumbers(matrix))    