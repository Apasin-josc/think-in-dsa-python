""" 
You are given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2 
"""

from typing import List

class Solution:
    def maxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutives = 0
        counter = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
                max_consecutives = max(max_consecutives, counter)
            elif nums[i] == 0:
                counter = 0
        
        return max_consecutives


sol = Solution()
print(sol.maxConsecutiveOnes([1,1,0,1,1,1]))
#print(sol.maxConsecutiveOnes([1,0,1,1,0,1]))


"""
T: O(n)
S: O(1)
"""
