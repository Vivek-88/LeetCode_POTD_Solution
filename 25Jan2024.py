from ast import List


class Solution:
    def f(self,s1:str,s2:str,i:int,j:int,dp:List[List[int]]) :
        if(i>=len(s1) or j>=len(s2)) :
            return 0
        if(dp[i][j]!=-1) :
            return dp[i][j]
        f1 = self.f(s1,s2,i+1,j,dp)
        f2 = self.f(s1,s2,i,j+1,dp)
        ans = max(f1,f2)
        if(s1[i]==s2[j]) :
            ans=max(ans,self.f(s1,s2,i+1,j+1,dp)+1)
        dp[i][j]=ans
        return ans
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1]*len(text2) for _ in range(len(text1))]
        return self.f(text1,text2,0,0,dp)