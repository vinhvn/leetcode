class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        length = rowIndex + 1
        prev = [1] * length
        curr = [1] * length
        for i in range(2, length):
            for j in range(1, i):
                curr[j] = prev[j-1] + prev[j]
            prev = curr.copy()
        return curr
