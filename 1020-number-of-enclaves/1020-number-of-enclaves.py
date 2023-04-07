class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        count = 0

        def dfs(i,j):
            if i<0 or i>=n or j<0 or j>=m or not grid[i][j]:
                return 
            
            grid[i][j]=0

            up = dfs(i-1,j)
            down = dfs(i+1,j)
            left = dfs(i,j-1)
            right = dfs(i,j+1)
            return up and down and left and right
            
            
        for i in range(n):
            if grid[i][0]:
                dfs(i,0)
            if grid[i][m-1]:
                dfs(i,m-1)
        for j in range(m):
            if grid[0][j]:
                dfs(0,j)
            if grid[n-1][j]:
                dfs(n-1,j)

        return sum([i.count(1) for i in grid])

        