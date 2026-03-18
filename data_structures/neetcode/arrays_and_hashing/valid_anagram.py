""" 
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order 
of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true

Example 2:
Input: s = "jar", t = "jam"
Output: false 
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        if len(s) != len(t):
            return False


        for c in s:
            if c in s_map:
                s_map[c] += 1
            else:
                s_map[c] = 1

        for c in t:
            if c in t_map:
                t_map[c] += 1
            else:
                t_map[c] = 1


        if s_map.items() == t_map.items():
            return True
        else:
            return False
        
sol = Solution()
print(sol.isAnagram("racecar", "carrace"))

#T: O(n)
#S: O(n)