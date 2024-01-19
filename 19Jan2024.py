# Problem Link :- https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, mat: List[List[int]]) -> int:
        ans = float(inf)
        n,m = len(mat),len(mat[0])
        
        # print(n,"",m)
        dp = [[0]*(m+5) for _ in range(m+5)]
        
        for i in range(n-1,-1,-1) :
            for j in range(m) :
                # print(mat[i][j],"",dp[i][j])
                dp[i][j] = dp[i+1][j]
                if(self.isValid(i+1,j-1,n,m)) :
                    dp[i][j]=min(dp[i][j],dp[i+1][j-1])
                
                if(self.isValid(i+1,j+1,n,m)) :
                    dp[i][j]=min(dp[i][j],dp[i+1][j+1])
                
                dp[i][j]+=mat[i][j]
                if(i==0) :
                    ans=min(ans,dp[i][j])
        return ans
    
    def isValid(self,i,j,n,m) -> bool:
        return (i>=0 and j>=0 and i<n and j<m)