class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n=len(questions)
        @cache
        def dfs(i):
            if i>=n:
                return 0
            return max(questions[i][0]+dfs(i+questions[i][1]+1),dfs(i+1))
        return dfs(0)