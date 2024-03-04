from ast import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        j=len(tokens)-1
        ans=0
        i=0
        score=0
        while(i<=j) :
            if(power>=tokens[i]) :
                power-=tokens[i]
                i+=1
                score+=1
            elif(score>0) :
                power+=tokens[j]
                j-=1
                score-=1
            else :
                break
            ans = max(score,ans)
        return ans