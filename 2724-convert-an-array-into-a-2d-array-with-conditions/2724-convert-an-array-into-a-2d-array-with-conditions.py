class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        current=nums
        ans=[]
        while len(current)>0:
            temp=list(set(current))
            for i in temp:
                current.remove(i)
            ans.append(temp)
        return ans