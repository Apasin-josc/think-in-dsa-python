from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            print(nums_map)
            if complement in nums_map:
                return[i, nums_map[complement]]
            else:
                nums_map[num] = i
        
        return []


    def twoSumNaive(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range( i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return[i, j]
        
        return []

sol = Solution()
print(sol.twoSum([3,4,5,6], 7))
print(sol.twoSumNaive([3,4,5,6], 7))

"""
T: O(n)
S: O(n)
"""


"""
T: O(n²)
S: O(1)
"""
