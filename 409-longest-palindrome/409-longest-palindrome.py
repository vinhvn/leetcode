class Solution:
    def longestPalindrome(self, s: str) -> int:
        charCount = collections.Counter(s)

        res = 0
        oddAdded = False
        for count in charCount.values():
            res += count // 2 * 2
            if not oddAdded and count % 2 == 1:
                oddAdded = True
                res += 1

        return res
