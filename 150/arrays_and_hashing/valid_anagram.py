from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_map = Counter(s)
        t_map = Counter(t)
        
        if s_map.items() != t_map.items():
            return False
        
        return True
        
    

sol = Solution()
print(sol.isAnagram("racecar", "carrace"))
print(sol.isAnagram("jar", "jam"))

"""
T: O(n)
S: O(n)
"""
