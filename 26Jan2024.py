# Problem Link :- https://leetcode.com/problems/out-of-boundary-paths/

from ast import List


class Solution:
    mod = int(1000000007)
    def add(self,a:int,b:int) :
        # print((a+b)%self.mod)
        return ((a+b)%self.mod)
    def f(self,m:int,n:int,i:int,j:int,step:int,dp:List[List[List[int]]]) :
        if(step<0) :
            return 0
        if(i<0 or i>=m or j<0 or j>=n) :
            return 1
        if(dp[i][j][step]!=-1) :
            return dp[i][j][step]
        f1 = self.f(m,n,i+1,j,step-1,dp)
        f2 = self.f(m,n,i,j+1,step-1,dp)
        f3 = self.f(m,n,i-1,j,step-1,dp)
        f4 = self.f(m,n,i,j-1,step-1,dp)
        dp[i][j][step]=self.add(self.add(f1,f2),self.add(f3,f4))
        return dp[i][j][step]
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[[-1]*(maxMove+1) for _ in range(n)] for _ in range(m)]
        return self.f(m,n,startRow,startColumn,maxMove,dp)
        