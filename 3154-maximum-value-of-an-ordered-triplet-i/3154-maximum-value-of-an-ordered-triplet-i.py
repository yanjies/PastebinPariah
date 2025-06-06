class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n=len(nums)
        suf_max=[0]*(n+1)
        for i in range(n-1,-1,-1):
            suf_max[i]=max(suf_max[i+1],nums[i])
        ans=pre_max=0
        for j,x in enumerate(nums):
            ans=max(ans,(pre_max-x)*suf_max[j+1])
            pre_max=max(pre_max,x)
        return ans