@cache
def dfs(i,c):
    if i==0:
        return 0 if c==0 else inf
    if c<i*i:
        return dfs(i-1,c)
    return min(dfs(i-1,c),dfs(i,c-i*i)+1)

class Solution:
    def numSquares(self, n: int) -> int:
        target=isqrt(n)
        return dfs(target,n)