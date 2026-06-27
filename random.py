from typing import List

class Sandbox:
    def learningLambda(self, nums: List[int]) -> List[int]:
        above_15 = [x for x in nums if x > 15]
        print(above_15)
        
    """
    sorted(nums, key=lambda x: x)
    nums.sort(key=lambda num: num > 15)
    closest = min(nums, key=lambda num: abs(num - 15))
    farthest = max(nums, key=lambda num: abs(num - 15))
    """
    
        
    

learning = Sandbox()
print(learning.learningLambda([20, 13, 10, 31, 14]))