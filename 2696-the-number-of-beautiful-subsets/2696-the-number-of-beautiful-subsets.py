class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        ans=0
        n=len(nums)
        cnt=defaultdict(int)

        def dfs(i):
            if i==n:
                nonlocal ans
                ans+=1
                return
            
            dfs(i+1)
            x=nums[i]
            if cnt[x-k]==0 and cnt[x+k]==0:
                cnt[x]+=1
                dfs(i+1)
                cnt[x]-=1
            
        dfs(0)
        return ans-1