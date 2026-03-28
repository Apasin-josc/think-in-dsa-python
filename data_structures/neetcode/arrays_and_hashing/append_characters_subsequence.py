"""
You are given two strings s and t consisting of only lowercase English letters.
Return the minimum number of characters that need to be appended to the end of s so that t
becomes a subsequence of s.
A subsequence is a string that can be derived from another string by deleting some or no 
characters without changing the order of the remaining characters.

Example 1:
Input: s = "coaching", t = "coding"
Output: 4
Explanation: Append the characters "ding" to the end of s so that s = "coachingding".
Now, t is a subsequence of s (coachingding).
It can be shown that appending any 3 characters to the end of s will never make t a subsequence.

Example 2:
Input: s = "abcde", t = "a"
Output: 0
Explanation: t is already a subsequence of s ("abcde").

Example 3:
Input: s = "z", t = "abcde"
Output: 5
Explanation: Append the characters "abcde" to the end of s so that s = "zabcde".
Now, t is a subsequence of s (zabcde).
It can be shown that appending any 4 characters to the end of s will never make t a subsequence. 
"""

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        """  counter = 0 """
        for j in range(len(s)):
            if i < len(t) and s[j] == t[i]:
                i += 1
        
        """ list_s = []
        list_t = []
        for c in s:
            list_s.append(c)
        
        for c in t:
            list_t.append(c) """
        

        """ for j in range(i, len(t)):
            list_s.append(list_t[j])
            counter += 1 """
        
        return len(t) - i

sol = Solution()
print(sol.appendCharacters("coaching", "coding"))