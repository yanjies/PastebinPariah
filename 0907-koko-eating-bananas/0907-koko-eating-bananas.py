from bisect import bisect_left,bisect_right
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right=max(piles)
        check=lambda k : sum(ceil(pile/k) for pile in piles)<= h
        return bisect_left(range(1,right),True,key=check)+1