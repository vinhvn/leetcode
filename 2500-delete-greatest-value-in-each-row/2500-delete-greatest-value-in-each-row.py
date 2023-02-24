class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()

        res = 0
        for _ in range(len(grid[0])):
            maxSoFar = -math.inf
            for row in grid:
                maxSoFar = max(maxSoFar, row.pop())
            res += maxSoFar
    
        return res    
