class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        ans=[]
        p=1
        while p<=n and p<=k//2:
            ans.append(p)
            p+=1
        i=0
        while p<=n:
            ans.append(k+i)
            i+=1
            p+=1
        return sum(ans)
