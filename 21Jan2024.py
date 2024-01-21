# Problem Link :- https://leetcode.com/problems/house-robber/

from ast import List


class Solution:
    def f(self,a : List[int],i :int, j: int,dp : List[List[int]]) -> int :
        if(i>=len(a)) :
            return 0
        
        if(dp[i][j]!=-1) :
            return dp[i][j]
        f1 = self.f(a,i+1,0,dp)
        ans=f1
        if(j==0) :
            f2 = self.f(a,i+1,1,dp)+a[i]
            ans=max(ans,f2)
        dp[i][j]=ans
        return ans
        
    def rob(self, nums: List[int]) -> int:
        dp = [[-1]*(2) for _ in range(len(nums))]
        return self.f(nums,0,0,dp)