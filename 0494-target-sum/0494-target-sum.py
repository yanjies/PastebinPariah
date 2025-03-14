class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i,t):
            if i<0:
                return 0
            if i==0 and t==0:
                return 1
            return dfs(i-1,t-nums[i-1])+dfs(i-1,t+nums[i-1])
        return dfs(len(nums),target)