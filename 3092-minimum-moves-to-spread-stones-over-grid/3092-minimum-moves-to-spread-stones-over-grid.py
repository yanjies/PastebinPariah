class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        source=[]
        target=[]

        for i,row in enumerate(grid):
            for j,cnt in enumerate(row):
                if cnt>1:
                    source.extend([(i,j)]*(cnt-1))
                elif cnt==0:
                    target.append((i,j))

        ans=inf
        for s in permutations(source):
            dis_sum=0
            for (x1,y1),(x2,y2) in zip(s,target):
                dis_sum+=abs(x1-x2)+abs(y1-y2)
            ans=min(ans,dis_sum)
            
        return ans