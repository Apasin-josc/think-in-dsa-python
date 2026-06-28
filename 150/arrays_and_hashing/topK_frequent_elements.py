from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1
        
        arr = []
        for key, value in map.items():
            arr.append([key, value])
            
        arr.sort(key=lambda x: x[1])
        
        ans = []
        for _ in range(k):
            ans.append(arr.pop()[0])
        
        return ans
    
    def topKFrequentOld(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1
        
        arr = []
        for key, value in map.items():
            arr.append([value, key])
        arr.sort()

        ans = []
        while len(ans) < k:
            ans.append(arr.pop()[1])
        
        return ans
            
    

sol = Solution()
#print(sol.topKFrequent([1,2,2,2,2,2,3,3,3,3,3,3,3,3,3], 2))
print(sol.topKFrequentOld([1,2,2,2,2,2,3,3,3,3,3,3,3,3,3], 2))