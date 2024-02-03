from ast import List


class Solution:
    
    def f(self,a:List[int],i:int,k:int,dp:List[int]) :
        if(i>=len(a)) :
            return 0
        if(dp[i]!=-1) :
            return dp[i]
        ans,mx,val,l=0,0,0,1
        for j in range(i,len(a)) :
            mx=max(mx,a[j])
            if(l>k) :
                break
            # print(val,mx)
            f1 = self.f(a,j+1,k,dp) + (l*mx)
            ans=max(ans,f1)
            # print(ans)
            l+=1
        dp[i]=ans
        return ans
    
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [-1]*(len(arr))
        return self.f(arr,0,k,dp)