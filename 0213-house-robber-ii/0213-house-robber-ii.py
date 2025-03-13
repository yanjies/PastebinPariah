class Solution:
    def sub_rob(self,nums:List[int]):
        @cache
        def dfs(i):
            if i<0:
                return 0
            return max(dfs(i-1),dfs(i-2)+nums[i])
        return dfs(len(nums)-1)

    def rob(self, nums: List[int]) -> int:
        return max(nums[0]+self.sub_rob(nums[2:-1]),self.sub_rob(nums[1:]))