class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        ans=[]
        path=[]

        def dfs(start,i):
            if i==n:
                ans.append(path.copy())
                return
            t=s[start:i+1]
            if t==t[::-1]:
                path.append(t)
                dfs(i+1,i+1)
                path.pop()
            if i<n-1:
                dfs(start,i+1)
        dfs(0,0)
        return ans 
        