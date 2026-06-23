from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_set = set()
        for num in nums:
            # O(1) because a set hashes the values and allocates them in a specific location
            if num in list_set:
                return True
            list_set.add(num)
        
        return False

    

sol = Solution()
print(sol.hasDuplicate([1,2,3]))


"""
T: O(n)
S: O(n)
"""
