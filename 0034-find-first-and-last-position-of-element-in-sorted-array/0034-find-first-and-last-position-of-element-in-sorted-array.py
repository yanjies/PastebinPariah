from bisect import bisect_left,bisect_right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        idx=bisect_left(nums,target)
        if idx>=len(nums) or nums[idx]!=target:
            return [-1,-1]
        return [bisect_left(nums,target),bisect_right(nums,target)-1]