""" 
Given an integer array nums, return true if any value appears more than once in the array, otherwise return
false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false 
"""

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_numbers = set()
        for num in nums:
            if num in seen_numbers:
                return True
            seen_numbers.add(num)
        
        return False
    
sol = Solution()

print(sol.hasDuplicate([1,2,3,3]))
print(sol.hasDuplicate([1,2,3,4]))

#T: O(n)
#S: O(n)
