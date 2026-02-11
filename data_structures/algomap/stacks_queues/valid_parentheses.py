"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false 
"""
from typing import List
class Solution:
    def validParenthesis(self, s: str) -> bool:
        
        hashmap = {")": "(", "}": "{", "]": "["}
        stk = []
 
        for c in s:
            if c not in hashmap:
                stk.append(c)
            else:
                if not stk:
                    return False
                else:
                    popped = stk.pop()
                    if popped != hashmap[c]:
                        return False
 
        return not stk

 
    
    def findInStack(stack: List[str]) -> int:
        pass
        

sol = Solution()
print(sol.validParenthesis("()"))
print(sol.validParenthesis("()[]{}"))
print(sol.validParenthesis("(]"))
print(sol.validParenthesis("([])"))
print(sol.validParenthesis("([)]"))
print(sol.validParenthesis("([])"))
