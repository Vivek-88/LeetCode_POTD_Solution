class Solution:
    def minimumLength(self, s: str) -> int:
        i=0
        j=len(s)-1
        while(i<j) :
            if(s[i]==s[j]) :
                idx=i
                while(i<j and s[idx]==s[i]) :
                    i+=1
                while(j>=i and s[idx]==s[j]) :
                    j-=1
            else :
                break
        
        return j-i+1