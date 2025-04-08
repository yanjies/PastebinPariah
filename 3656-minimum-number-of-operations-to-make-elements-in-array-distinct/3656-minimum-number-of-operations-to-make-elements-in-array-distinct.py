class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        saw=set()
        for i in range(len(nums)-1,-1,-1):
            x=nums[i]
            if x in saw:
                return i//3+1
            saw.add(x)
        return 0
        