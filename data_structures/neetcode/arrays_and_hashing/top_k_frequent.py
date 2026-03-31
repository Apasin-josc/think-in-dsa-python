""" 
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

Example 1:
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

Example 2:
Input: nums = [7,7], k = 1
Output: [7] 
"""

from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1
        
        arr = []
        for key, value in map.items():
            arr.append([key, value])
        
        res = []
        """ while len(res) < k:
            res.append(arr.pop()[0]) """
            
        for i in range(len(arr)):
            if k > 0:
                res.append(arr.pop()[0])
                k -= 1
        
        return res
        
sol = Solution()
print(sol.topKFrequent([1,2,2,3,3,3,3,3], 2))
print(sol.topKFrequent([7,7], 1))

#T: O(n log n)
#S: O(n)
