class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum=list(accumulate(nums,initial=0))
        cnt=defaultdict(int)
        ans=0
        for x in presum:
            ans+=cnt[x-k]
            cnt[x]+=1
        return ans