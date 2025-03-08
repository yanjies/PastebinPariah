class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans=[]
        path=[]

        def dfs(i,t):
            if t==0:
                ans.append(path.copy())
                return 
             
            if i>=len(candidates) or t<candidates[i]:
                return
            
            # 不选
            dfs(i+1,t)

            # 选
            path.append(candidates[i])
            dfs(i,t-candidates[i])
            path.pop()
        
        dfs(0,target)
        return ans