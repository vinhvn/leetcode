class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) < k:
            return s[::-1]
        elif k == 1:
            return s

        chars = list(s)
        for i in range(0, len(s), 2*k):
            l, r = i, min(len(s) - 1, i + k - 1)
            while l < r:
                chars[l], chars[r] = chars[r], chars[l]
                l += 1
                r -= 1

        return "".join(chars)
