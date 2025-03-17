from bisect import bisect_left,bisect_right

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans=[]
        n=len(potions)
        for spell in spells:
            target=ceil(success/spell)
            ans.append(n-bisect_left(potions,target))
        return ans