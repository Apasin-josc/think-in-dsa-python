from typing import List

def longestConsecutiveSequence(nums: List[int]) -> int:
    res = 0
    store = set(nums)

    for num in nums:
            streak, curr = 0, num
            while curr in store:
                streak += 1
                curr += 1
            res = max(res, streak)
    return res            

print(longestConsecutiveSequence([2,20,4,10,3,4,5]))


"""
T: O(n^2)
S: O(n)
"""
