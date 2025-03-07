class NumArray:

    def __init__(self, nums: List[int]):
        self.presum=list(accumulate(nums,initial=0))

    def sumRange(self, left: int, right: int) -> int:
        return self.presum[right+1]-self.presum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)