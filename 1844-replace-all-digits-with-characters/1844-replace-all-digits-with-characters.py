class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(c, x):
            return chr(ord(c) + x)
        
        if len(s) == 1:
            return s

        chars = list(s)
        for i in range(1, len(s), 2):
            chars[i] = shift(chars[i-1], int(chars[i]))
        
        return "".join(chars)
