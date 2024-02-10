class Solution:
    def countSubstrings(self, s: str) -> int:
        def f(s1:str,i:int,j:int) :
            if(i>=j) :
                return 1
            if(dp[i][j]!=-1) :
                return dp[i][j]
            ans=0;
            if(s1[i]==s1[j]) :
                ans+=f(s,i+1,j-1)
            dp[i][j]=ans
            return ans
        n = len(s)
        dp = [[-1]*n for _ in range(n)]
        ans=0
        for i in range(n) :
            for j in range(i,n) :
                ans+=f(s,i,j)
        return ans