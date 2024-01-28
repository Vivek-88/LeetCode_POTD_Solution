from ast import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n,m = len(matrix),len(matrix[0])
        dp = [[0]*m for _ in range(n)]
        
        for i in range(n) :
            sum=0
            for j in range(m) :
                sum+=matrix[i][j]
                dp[i][j]=sum
                if(i!=0) :
                    dp[i][j]+=dp[i-1][j]
        
        ans=0
        for i in range(n) :
            for j in range(m) :
                for k in range(i,n) :
                    for l in range(j,m) :
                        val=dp[k][l]
                        if(j-1>=0) :
                            val-=dp[k][j-1]
                        if(i-1>=0) :
                            val-=dp[i-1][l]
                        if(j-1>=0 and i-1>=0) :
                            val+=dp[i-1][j-1]
                        if(val==target) :
                            ans+=1
        return ans