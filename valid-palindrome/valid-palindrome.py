import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        d = {}
        
        clean = re.sub(r'[^a-zA-Z0-9]+', '', s).lower()
        
        l = 0
        r = len(clean) - 1
        while (l < r):
            if clean[l] != clean[r]:
                return False
            l += 1
            r -= 1
        
        return True