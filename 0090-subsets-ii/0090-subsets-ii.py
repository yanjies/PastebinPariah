class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        path=[]
        nums.sort()
        n=len(nums)

        def dfs(i):
            if i==n:
                ans.append(path.copy())
                return
            
            x=nums[i]
            # select
            path.append(x)
            dfs(i+1)
            path.pop()

            # unselect
            i+=1
            while i<n and nums[i]==x:
                i+=1
            dfs(i)
        dfs(0)
        
        return ans