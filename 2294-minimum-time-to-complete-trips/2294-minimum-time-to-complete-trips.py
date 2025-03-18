from bisect import bisect_left,bisect_right
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        right=ceil(totalTrips/len(time))*max(time)
        check=lambda k: sum(k//t for t in time)>=totalTrips
        return bisect_left(range(right),True,key=check)