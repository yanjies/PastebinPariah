class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])

        @cache
        def dfs(i,j):
            if i==0 and j==0:
                return 0
            if i<0 or j<0:
                return inf
            
            return min(dfs(i-1,j)+grid[i-1][j],dfs(i,j-1)+grid[i][j-1])
        
        return dfs(m-1,n-1)+grid[m-1][n-1]