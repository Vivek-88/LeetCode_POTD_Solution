class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        f1=0;
        f2=0;
        for i in range(0,len(s)) :
            if(self.isVowel(s[i])) :
                if i<len(s)/2 :
                    f1+=1;
                else :
                    f2+=1;
        return f1==f2;
        
    
    def isVowel(self, c: chr) -> bool:
        return c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or c=='A' or c=='E' or c=='I' or c=='O' or c=='U';