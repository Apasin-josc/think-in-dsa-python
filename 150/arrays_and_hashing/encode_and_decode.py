from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return '☠️'
        encoded_message = '🦖'.join(strs)
        return encoded_message
        
    
    def decode(self, s: str) -> List[str]:
        if s == '☠️':
            return []
        
        return s.split('🦖')
    

sol = Solution()
encoded_message = sol.encode(["Hello", "World"])
print(encoded_message)
decoded_message = sol.decode(encoded_message)
print(decoded_message)
