class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum=list(accumulate(nums,initial=0))
        ans=0
        cnt=defaultdict(int)
        for s in presum:
            ans+=cnt[s-k]
            cnt[s]+=1
        return ans