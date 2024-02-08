from cmath import inf


class Solution:
    def numSquares(self, n: int) -> int:
        def f(v,dp) :
            if(v==0) :
                return 0
            if(dp[v]!=-1) :
                return dp[v]
            ans = inf
            for i in range(1,v+1) :
                if(i*i>v) :
                    break
                f1 = f(v-(i*i),dp)
                ans=min(ans,f1+1)
            dp[v]=ans
            return ans
        dp = [-1]*(n+1)
        return f(n,dp)