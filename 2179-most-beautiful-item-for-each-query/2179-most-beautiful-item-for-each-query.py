from bisect import bisect_right
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda q:q[0])
        
        # 原地前缀max
        for i in range(1,len(items)):
            items[i][1]=max(items[i-1][1],items[i][1])
        
        ans=[]
        # bisect的二维数组写法
        for q in queries:
            index=bisect_right(items,q,key=lambda p:p[0])-1
            if index<0:
                ans.append(0)
            else:
                ans.append(items[index][1])
        return ans

