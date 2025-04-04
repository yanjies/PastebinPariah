class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        ans=s=0
        cnt=defaultdict(int)
        cnt[0]=1
        for n in nums:
            s^=n
            ans+=cnt[s]
            cnt[s]+=1
        return ans
            