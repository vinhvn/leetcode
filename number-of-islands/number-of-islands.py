class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        m = len(grid)
        n = len(grid[0])
        islands = 0
        
        def dfs(y, x):
            if (y < 0 or y >= m) or (x < 0 or x >= n) or grid[y][x] == "0":
                return
            grid[y][x] = "0"
            for dy, dx in directions:
                dfs(y+dy, x+dx)
        
        for y in range(m):
            for x in range(n):
                if grid[y][x] == "1":
                    islands += 1
                    dfs(y, x)
        
        return islands
            