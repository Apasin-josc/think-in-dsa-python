""" 
You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false 
"""
from typing import List
class Solution:
    
    """ 
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target in row:
                return True
        return False 
    T: O(m*x)
    S: O(1)
    """
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        t = m * n
        l = 0
        r = t - 1
        while l <= r:
            M = (l + r) // 2
            ri = M // n
            rj = M % n
            val = matrix[ri][rj]
            if val == target:
                return True
            elif val < target:
                l = M + 1
            else:
                r = M - 1
        
        return False
    """
    T: O(log(m*n))
    S: O(1)
    """
            
            
    
sol = Solution()
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))                                                                                                                                                                                                         
