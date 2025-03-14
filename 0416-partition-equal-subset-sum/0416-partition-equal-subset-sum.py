class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target=sum(nums)
        if target%2:
            return False
        target//=2

        # @cache
        # def dfs(i,c):
        #     if i<0:
        #         return True if c==0 else False
        #     if c<nums[i]:
        #         return dfs(i-1,c)
        #     return dfs(i-1,c) or dfs(i-1,c-nums[i])
        
        # return dfs(len(nums)-1,target)

        n=len(nums)
        f=[[False]*(target+1) for _ in range(n+1)]
        f[0][0]=True
        for i,x in enumerate(nums):
            for c in range(target+1):
                if c<x:
                    f[i+1][c]=f[i][c]
                else:
                    f[i+1][c]=f[i][c] or f[i][c-x]
        return f[n][target]