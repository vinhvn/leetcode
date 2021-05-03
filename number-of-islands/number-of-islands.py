class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        res = 0
        m, n = (len(grid), len(grid[0]))
        
        # helper to check bounds
        def inBounds(x, y):
            return (x >= 0 and x < n and y >= 0 and y < m)
        
        # helper to get adjacent grid slots
        def getAdj(x, y):
            d = [(1,0), (-1,0), (0,1), (0,-1)]
            return [(x+i, y+j) for (i,j) in d if inBounds(x+i, y+j)]
        
        def dfs(x, y):
            grid[y][x] = "0"
            for (i,j) in getAdj(x,y):
                if grid[j][i] == "1":
                    dfs(i,j)
        
        for j in range(m):
            for i in range(n):
                if grid[j][i] == "1":
                    res += 1
                    dfs(i,j)
        
        return res