""" 
You are given an array arr, replace every element in that array with the greatest element among the 
elements to its right, and replace the last element with -1.
After doing so, return the array.

Example 1:
Input: arr = [2,4,5,3,1,2]
Output: [5,5,3,2,2,-1]

Example 2:
Input: arr = [3,3]
Output: [3,-1] 
"""
from typing import List
from typing import List

class Solution:
    def greatest_element(self, arr: List[int]) -> List[int]:
        max_so_far = -1
        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = max_so_far          
            max_so_far = max(max_so_far, current)
        return arr

sol = Solution()
print(sol.greatest_element([2,4,5,3,1,2]))

                
            

sol = Solution()
print(sol.greatest_element([2,4,5,3,1,2]))

#T: O(n)
#S: O(1)
