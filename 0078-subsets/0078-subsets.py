class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        path=[]
        n=len(nums)
        def dfs(i):
            if i>n:
                return
            ans.append(path.copy())
            for j in range(i,n):
                path.append(nums[j]) #选
                dfs(j+1)
                path.pop() #不选
        dfs(0)
        return ans