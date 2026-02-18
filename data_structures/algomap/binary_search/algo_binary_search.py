"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
 
Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1 
"""
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        L = 0
        R = N - 1
        while L <= R:
            M = (L + R) // 2
            if nums[M] == target:
                return M
            elif target < nums[M]:
                R = M - 1
            else:
                L = M + 1
        
        return -1

sol = Solution()
print(sol.search([-1,0,3,5,9,12], 9))