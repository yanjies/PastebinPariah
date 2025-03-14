class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target=sum(nums)
        if target%2:
            return False
        
        target//=2
        @cache
        def dfs(i,c):
            if i<0:
                return True if c==0 else False
            if c<nums[i]:
                return dfs(i-1,c)
            return dfs(i-1,c) or dfs(i-1,c-nums[i])
        
        return dfs(len(nums)-1,target)