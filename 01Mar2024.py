class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one =0
        for i in range(len(s)) :
            if(s[i]=='1') :
                one+=1
        
        ans=""
        for i in range(len(s)-1) :
            if(one>1) :
                ans+="1"
                one-=1
            else :
                ans+="0"
        return ans+"1"