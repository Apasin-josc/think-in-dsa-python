""" 
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, 
but the order of the characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
Input: strs = ["x"]
Output: [["x"]]

Example 3:
Input: strs = [""]
Output: [[""]] 
"""
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for str in strs:
            key = "".join(sorted(str))
            if key not in hashMap:
                hashMap[key] = []
            hashMap[key].append(str)
        
        print(hashMap)
        return list(hashMap.values())  
    
    #T(O) = O(m * nlogn)
    #S(O) = O(m * n)  
    
    def groupAnagrams_pro(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
    
    #T(O) = O(m * n)
    #S(O) = O(m)
        
sol = Solution()
print(sol.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
