class Solution:
    def totalNQueens(self, n: int) -> int:
        ans=0
        path=[]

        def isvalid(r,c):
            for R in range(r):
                C=path[R]
                if C-c==R-r or C-c==r-R:
                    return False
            return True
        
        def dfs(r,s):
            if r==n:
                nonlocal ans
                ans+=1
            
            for c in s:
                if isvalid(r,c):
                    path.append(c)
                    dfs(r+1,s-{c})
                    path.pop()

        dfs(0,set(range(n)))
        return ans