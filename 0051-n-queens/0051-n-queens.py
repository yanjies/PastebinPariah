class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        path=[]

        def isvalid(r,c):
            for R in range(r):
                C=path[R]
                if R-r==C-c or R-r==c-C:
                    return False
            return True

        def dfs(r,s):
            if r==n:
                # ans.append(path.copy())
                ans.append(["."*c+"Q"+"."*(n-c-1) for c in path])
                return
            
            for c in s:
                if isvalid(r,c):
                    path.append(c)
                    dfs(r+1,s-{c})
                    path.pop()
        
        dfs(0,set(range(n)))
        return ans