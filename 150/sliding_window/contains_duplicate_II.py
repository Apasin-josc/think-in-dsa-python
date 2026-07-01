class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0
        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            
            if nums[R] in window:
                return True
            
            window.add(nums[R])
        
        return False

"""
T: O(n)
S: O(k) where k is the fixed size of the window
"""
