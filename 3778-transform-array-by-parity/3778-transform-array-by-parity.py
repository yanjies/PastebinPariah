class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[1]*n
        i=0
        for num in nums:
            if num%2==0:
                ans[i]=0
                i+=1
        return ans
