class Solution:
    def subSlideWindow(self,word,k):
        # ans=0
        cnt1=defaultdict(int)
        # cnt2=0
        # left=0
        ans=cnt2=left=0

        for w in word:
            if w in 'aeiou':
                cnt1[w]+=1
            else:
                cnt2+=1
            while len(cnt1)==5 and cnt2>=k:
                current=word[left]
                if current in 'aeiou':
                    cnt1[current]-=1
                    if cnt1[current]==0:
                        del cnt1[current]
                else:
                    cnt2-=1
                left+=1
            ans+=left #这里真的是天才啊！！！
        return ans

    def countOfSubstrings(self, word: str, k: int) -> int:
        return self.subSlideWindow(word,k)-self.subSlideWindow(word,k+1)