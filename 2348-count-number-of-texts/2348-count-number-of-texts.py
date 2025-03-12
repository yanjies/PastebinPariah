class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        alphabet=[0,0,3,3,3,3,3,4,3,4]
        MOD=1_000_000_007
        @cache
        def dfs(i,k):
            if i<0:
                return 0
            if i==0:
                return 1
            return (sum(dfs(i-j,k) for j in range(1,k+1)))%MOD
        ans=1
        l=r=0
        while r<len(pressedKeys):
            if pressedKeys[r]==pressedKeys[l]:
                r+=1
            else:
                ans*=dfs(r-l,alphabet[int(pressedKeys[l])])
                ans%=MOD
                l=r

        ans*=dfs(r-l,alphabet[int(pressedKeys[l])])
        ans%=MOD
        return ans