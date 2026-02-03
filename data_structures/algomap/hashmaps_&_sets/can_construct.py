"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters
from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

 
Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true 
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        counter = len(ransomNote)
        
        for c in magazine:
            if c in dict:
                dict[c] += 1
            else:
                dict[c] = 1
        
        for c in ransomNote:
            if c in dict and dict[c] > 0:
                dict[c] -= 1
                counter -= 1
        
        return True if counter == 0 else False     
    
    def oldMedefcanConstruct(self, ransomNote: str, magazine: str) -> bool:
        if not ransomNote:
            return True
        
        hashMap = {}
        for ch in magazine:
            hashMap[ch] = hashMap.get(ch, 0) + 1

        for ch in ransomNote:
            if hashMap.get(ch, 0) > 0:
                hashMap[ch] -= 1
            else:
                return False
        
        return True   
    
sol = Solution()
print(sol.canConstruct('aa', 'aab'))
print(sol.canConstruct('a', 'b'))
print(sol.canConstruct('aa', 'ab'))
