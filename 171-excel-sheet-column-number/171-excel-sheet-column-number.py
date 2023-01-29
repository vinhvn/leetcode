class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        def getNumber(char: str) -> int:
            return ord(char) - ord("A") + 1
        
        res = 0
        for i in range(len(columnTitle)):
            backwardsIndex = len(columnTitle) - 1 - i
            res += getNumber(columnTitle[i]) * (26 ** backwardsIndex)
        return res