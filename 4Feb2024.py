class Solution:
    def idx(self,s : str,i: int) :
        if(ord(s[i])>=ord('a')) :
            return ord(s[i])-ord('a')+26
        return ord(s[i])-ord('A')
    
    def minWindow(self, s: str, t: str) -> str:
        fre = [0]*52
        for i in range(len(t)) :
            fre[self.idx(t,i)]-=1
        strt=0
        end=0
        i,j,ans=0,0,inf
        while(j<len(s)) :
            isValid=True
            for f in fre :
                if(f<0) :
                    isValid=False
            if(isValid) :
                fre[self.idx(s,i)]-=1
                if(ans>j-i) :
                    ans=j-i
                    strt=i
                    end=j
                i+=1
            else :
                fre[self.idx(s,j)]+=1
                j+=1
        
        while(i<len(s)) :
            isValid=True
            for f in fre :
                if(f<0) :
                    isValid=False
            if(isValid) :
                fre[self.idx(s,i)]-=1
                if(ans>j-i) :
                    ans=j-i
                    strt=i
                    end=j
                i+=1
            else :
                break
        return s[strt:end]