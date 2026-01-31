"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. 
Each character in stones is a type of stone you have. 
You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0 
"""

from collections import Counter
class Solution:

    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict = Counter(jewels)
        counter = 0
        for stone in stones:
            if dict[stone]:
                counter += 1
        
        return counter

    def oldMeSolution(self, jewels: str, stones: str) -> int:
        dict = {}
        for s in stones:
            if s in dict:
                dict[s] += 1
            else:
                dict[s] = 1
        
        count = 0
        for j in jewels:
            if j in dict:
                count += dict.get(j, 0)
        
        return count
        

sol = Solution()
print(sol.numJewelsInStones("aA", "aAAbbbb"))
print(sol.numJewelsInStones("z", "ZZ"))
print(sol.oldMeSolution("aA", "aAAbbbb"))
print(sol.oldMeSolution("z", "ZZ"))