""" 
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in  O(n) time without using the division operation?

Example 1:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]

Example 2:
Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0] 
"""
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        ans = []
        i = 1
        z = 1
        for j in range(len(nums)):
            prefix.append(i)
            i *= nums[j]
        
        for j in range(len(nums) - 1, -1, -1):
            suffix.insert(0, z)
            z *= nums[j]
        
        for i in range(len(nums)):
            ans.append(prefix[i] * suffix[i])
        
        return ans
            
sol = Solution()
#print(sol.productExceptSelf([1,2,4,6])) #[48,24,12,8]
print(sol.productExceptSelf([-1,0,1,2,3]))


""" prefix.append(i) = 1
i = 1 *= 1 = 1

prefix.append(i) = 1
i = 1 *= 2 = 2

prefix.append(i) = 2
i = 2 *= 4 = 8

prefix.append(i) = 8
i = 8 *= 6 = 48 """