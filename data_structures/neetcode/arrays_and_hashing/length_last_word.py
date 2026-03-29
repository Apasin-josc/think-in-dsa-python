""" 
You are given a string s consisting of words and spaces, return the length of
the last word in the string.
A word is a maximal substring consisting of non-space characters only.
Note: A substring is a contiguous non-empty sequence of characters within a string.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6. 
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        my_list = s.split()
        if not my_list or not s:
            return 0
        
        last_word = my_list[-1]
        
        return len(last_word)
        
        
sol = Solution()
print(sol.lengthOfLastWord("Hello World"))
print(sol.lengthOfLastWord("   fly me   to   the moon  "))
print(sol.lengthOfLastWord("a"))
print(sol.lengthOfLastWord("    "))

#T: O(n)
#S: O(n)