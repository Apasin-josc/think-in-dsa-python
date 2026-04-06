""" 
Given an array of integers numbers that is sorted in non-decreasing order.
Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target
and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.
Your solution must use 
O(1)
O(1) additional space.

Example 1:
Input: numbers = [1,2,3,4], target = 3
Output: [1,2]
Explanation:
The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2]. 
"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1
        while L < R:
            sum = numbers[L] + numbers[R]
            if sum == target:
                return [L + 1, R + 1]
            elif sum < target:
                L += 1
            else:
                R -= 1
                
                
sol = Solution()
print(sol.twoSum([1,2,3,4], 3))

#T: O(n)
#S: O(1)
