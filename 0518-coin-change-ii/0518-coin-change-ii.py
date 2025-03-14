class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dfs(i,c):
            if i<0:
                return 1 if c==0 else 0
            if c<coins[i]:
                return dfs(i-1,c)
            return dfs(i-1,c)+dfs(i,c-coins[i])
        
        return dfs(len(coins)-1,amount)