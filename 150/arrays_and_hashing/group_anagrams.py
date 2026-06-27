from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[int]) -> List[int]:
        map = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key in map:
                map[key].append(word)
            else:
                map[key] = [word]
        
        return list(map.values())
    
    
    def groupAnagrams_pro(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
    
    
sol = Solution()
print(sol.groupAnagrams(["act","pots","tops","cat","stop","hat"]))