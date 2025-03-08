class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        path=[]

        def dfs(i,left):
            if i==n*2:
                ans.append(''.join(path.copy()))
                return
            
            if left<n:
                path.append('(')
                dfs(i+1,left+1)
                path.pop()
            
            # right=i-left
            if i-left<left:
                path.append(')')
                dfs(i+1,left)
                path.pop()

        dfs(0,0)
        return ans
