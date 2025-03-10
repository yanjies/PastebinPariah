class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dfs(i):
            if i==0:
                return 1
            if i<0:
                return 0
            return dfs(i-1)+dfs(i-2)
        return dfs(n)