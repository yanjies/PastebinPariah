class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        ans=0
        snum=str(num)
        for i in range(len(snum)-k+1):
            c=int(snum[i:i+k])
            if c!=0 and num % c==0:
                ans+=1
        return ans