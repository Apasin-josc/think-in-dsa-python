""" 
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false 
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        
        if len(s) != len(t):
            return False
        
        for char in s:
            if char in s_map:
                s_map[char] += 1
            else:
                s_map[char] = 1
        
        for char in t:
            if char in t_map:
                t_map[char] += 1
            else:
                t_map[char] = 1
        
        if s_map.items() != t_map.items():
            return False
        
        return True
        

sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))
print(sol.isAnagram("car", "rat"))
