class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits = [int(x) for x in str(n)]
        out = 0
        for i, d in enumerate(digits):
            out += -d if i % 2 else d
        return out