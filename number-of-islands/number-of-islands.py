class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def findIsland():
            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    if grid[y][x] == "1":
                        return (True, x, y)
            return (False,-1,-1)
        
        def destroy(x, y):
            # if already visited, return
            if grid[y][x] == "0":
                return
            
            # set to visited
            grid[y][x] = "0"
            
            # bounds check and recurse
            if (x - 1 >= 0):
                destroy(x-1, y)
            if (x + 1 < len(grid[0])):
                destroy(x+1, y)
            if (y - 1 >= 0):
                destroy(x, y-1)
            if (y + 1 < len(grid)):
                destroy(x, y+1)
            
        (found, x, y) = findIsland()
        numIslands = 0
        
        while found:
            numIslands += 1
            destroy(x,y)
            (found, x, y) = findIsland()
        
        return numIslands