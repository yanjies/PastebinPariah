class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        l,r=bounds[0][0]-original[0],bounds[0][1]-original[0]
        for i,bound in enumerate(bounds):
            l=max(l,bound[0]-original[i])
            r=min(r,bound[1]-original[i])
            if l>r:
                return 0
        return r-l+1