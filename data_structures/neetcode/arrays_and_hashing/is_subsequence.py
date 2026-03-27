""" 
You are given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some
(can be none) of the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "node", t = "neetcode"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false 
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for j in range(len(t)):
            if i < len(s) and s[i] == t[j]:  #python is going to read first the left side of the `AND`
                i += 1
        
        return True if len(s) == i else False
        
        
        

sol = Solution()
#print(sol.isSubsequence("node", "neetcode"))
print(sol.isSubsequence("abc", "aabbcc"))

#T: O(len(t))
#S: O(1)
