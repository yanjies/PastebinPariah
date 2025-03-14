# @cache
# def dfs(i,c):
#     if i==0:
#         return 0 if c==0 else inf
#     if c<i*i:
#         return dfs(i-1,c)
#     return min(dfs(i-1,c),dfs(i,c-i*i)+1)
N=10000
f=[[inf]*(N+1) for _ in range(isqrt(N)+1)]
f[0][0]=0
for i in range(1,len(f)):
    for c in range(N+1):
        if c<i*i:
            f[i][c]=f[i-1][c]
        else:
            f[i][c]=min(f[i-1][c],f[i][c-i*i]+1)

class Solution:
    def numSquares(self, n: int) -> int:
        target=isqrt(n)
        # return dfs(target,n)
        return f[target][n]