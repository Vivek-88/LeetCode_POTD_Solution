class Solution:
    def minSteps(self, s: str, t: str) -> int:
        fre = [0]*26
        for i in range(0,len(s)) :
            fre[ord(s[i])-ord('a')]+=1
            fre[ord(t[i])-ord('a')]-=1
        ans=0;
        for f in fre :
            if(f>0) :
                ans+=f
        return ans