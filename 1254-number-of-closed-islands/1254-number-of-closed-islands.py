class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        count = 0

        def dfs(grid, i,j):
            if grid[i][j]==1:
                return True
            if i<=0 or i>=m-1 or j<=0 or j>=n-1:
                return False
            grid[i][j]=1

            down = dfs(grid,i+1,j)
            up = dfs(grid,i-1,j)
            right = dfs(grid,i,j+1)
            left = dfs(grid,i,j-1)
            
            return up and down and left and right
             
        for i in range(1,m-1):
            for j in range(1,n-1):
                if grid[i][j]==0 and dfs(grid,i,j):
                    count+=1
        return count

