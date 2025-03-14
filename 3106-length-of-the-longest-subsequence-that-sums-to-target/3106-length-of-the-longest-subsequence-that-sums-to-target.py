class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        # @cache
        # def dfs(i,c):
        #     if i<0:
        #         return 0 if c==0 else -inf
        #     if c<nums[i]:
        #         return dfs(i-1,c)
        #     return max(dfs(i-1,c),dfs(i-1,c-nums[i])+1)
        
        # ans=dfs(len(nums)-1,target)

        n=len(nums)

        f=[[-inf]*(target+1) for _ in range(n+1)]
        f[0][0]=0

        for i,x in enumerate(nums):
            for c in range(target+1):
                if c<x:
                    f[i+1][c]=f[i][c]
                else:
                    f[i+1][c]=max(f[i][c],f[i][c-x]+1)
        
        ans=f[n][target]
        return ans if ans>-1 else -1
