from bisect import bisect_left,bisect_right

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n=len(nums)
        l=bisect_right(nums,-1)
        r=bisect_left(nums,1)
        return max(l,n-r)