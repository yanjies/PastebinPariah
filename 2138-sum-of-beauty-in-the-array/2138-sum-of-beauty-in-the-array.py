class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        max_pre=[0]*(n+1)
        min_suf=[0]*(n+1)
        min_suf[n]=inf

        for i in range(n):
            max_pre[i+1]=max(max_pre[i],nums[i])
        
        for i in range(n-1,-1,-1):
            min_suf[i]=min(min_suf[i+1],nums[i])

        for i in range(1,n-1):
            if max_pre[i]<nums[i]<min_suf[i+1]:
                ans+=2
            elif nums[i-1]<nums[i]<nums[i+1]:
                ans+=1

        return ans