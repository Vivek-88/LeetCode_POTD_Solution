class Solution:
    def closeStrings(self, w1: str, w2: str) -> bool:
        if(len(w1)!=len(w2)) :
            return False
        f1 = [0]*26
        f2 = [0]*26
        for i in range(0,len(w1)) :
            f1[ord(w1[i])-ord('a')]+=1
            f2[ord(w2[i])-ord('a')]+=1
        
        for i in range(0,26) :
            if(f1[i]==f2[i]) :
                f1[i]=f2[i]=-1
            else :
                if(f1[i]==0 or f2[i]==0) :
                    return False
        
        f1.sort()
        f2.sort()
        ct=0
        for i in range(0,26) :
            if(f1[i]!=f2[i]) :
                return False
            else :
                ct+=1
        
        if(ct%2==1) :
            return False
        return True