""" 
You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent 
characters.
Return the score of s.

Example 1:
Input: s = "code"
Output: 24
Explanation: The ASCII values of the characters in the given string are: 'c' = 99, 'o' = 111, 'd' = 100, and 'e' = 101.
The score of s will be: |111 - 99| + |100 - 111| + |101 - 100|.

Example 2:
Input: s = "neetcode"
Output: 65 
"""


class Solution:
    def scoreString(self, s: str) -> int:
        i = 0
        total = 0
        for j in range(1, len(s)):
            total += abs(ord(s[i]) - ord(s[j]))
            i += 1
        
        return total
    
sol = Solution()
print(sol.scoreString("code"))

#T(O) : O(n)
#S(O) : O(1)
