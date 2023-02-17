class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        return mul(*map(min, zip(*ops))) if ops else m * n