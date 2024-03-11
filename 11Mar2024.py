class Solution:
    def customSortString(self, order: str, s: str) -> str:
        fre = [0]*26
        for c in s :
            fre[ord(c)-ord('a')]+=1
        ans = ""
        for c in order :
            while(fre[ord(c)-ord('a')]>0) :
                ans+=c
                fre[ord(c)-ord('a')]-=1
        for i in range(26) :
            while(fre[i]>0) :
                ans+=chr(i+ord('a'))
                fre[i]-=1
        return ans