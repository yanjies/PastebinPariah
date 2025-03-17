from bisect import bisect_left,bisect_right

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()        
        ans=0
        n=len(nums)
        for i,num in enumerate(nums):
            l=bisect_left(nums,lower-num,i+1,n)
            r=bisect_right(nums,upper-num,i+1,n)
            ans+=(r-l)
        return ans