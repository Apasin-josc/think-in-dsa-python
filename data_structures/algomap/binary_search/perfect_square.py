""" 
Given a positive integer num, return true if num is a perfect square or false otherwise.
A perfect square is an integer that is the square of an integer. 
In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

Example 1:
Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

Example 2:
Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer. 
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        L = 0
        R = num
        while L <= R:
            
            M = (L + R) // 2
            M_SQUARED = M * M
            if M_SQUARED == num:
                return True
            elif M_SQUARED < num:
                L = M + 1
            else:
                R = M - 1
        
        return False

sol = Solution()
print(sol.isPerfectSquare(16))
print(sol.isPerfectSquare(14))