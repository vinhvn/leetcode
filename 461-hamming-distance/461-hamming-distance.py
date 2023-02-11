class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # XOR bits
        diff = x ^ y
        
        # count bits
        res = bin(diff).count("1")
        
        return res