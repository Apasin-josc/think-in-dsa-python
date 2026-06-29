from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        left_product = []
        for i in range(len(nums)):
            left_product.append(left)
            left *= nums[i]

        print(left_product)  

        right = 1
        right_product = []
        for j in range(len(nums) - 1, -1, -1):
            right_product.append(right)
            right *= nums[j]
        
        print(right_product)

        ans = []

        i, j = 0, len(nums) - 1
        for _ in range(len(nums)):
            ans.append((left_product[i] * right_product[j]))
            i += 1
            j -= 1
        
        return ans
        
sol = Solution()
print(sol.productExceptSelf([1,2,4,6]))
#[48,24,12,8]


"""
T: O(n)
S: O(n)
"""
