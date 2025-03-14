class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # @cache
        # def dfs(i,t):
        #     if i<0:
        #         return 0
        #     if i==0 and t==0:
        #         return 1
        #     return dfs(i-1,t-nums[i-1])+dfs(i-1,t+nums[i-1])
        # return dfs(len(nums),target)
        target+=sum(nums)
        if target<0 or target%2:
            return 0
        
        target//=2

        @cache
        def dfs(i,c):
            if i<0:
                return 1 if c==0 else 0
            if c<nums[i]:
                dfs(i-1,c)
            return dfs(i-1,c)+dfs(i-1,c-nums[i])
        
        return dfs(len(nums)-1,target)