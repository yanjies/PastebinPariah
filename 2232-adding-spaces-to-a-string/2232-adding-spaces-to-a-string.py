class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans=""
        start=0
        for end in spaces:
            ans+=s[start:end]
            ans+=" "
            start=end
        ans+=s[start:]
        return ans
        