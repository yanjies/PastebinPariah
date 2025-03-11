class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i):
            if i==0:
                return 1
            return sum([dfs(i-j) for j in nums if j<=i])
        return dfs(target)