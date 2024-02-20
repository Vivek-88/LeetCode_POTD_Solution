class Solution {
    public int maxSumAfterPartitioning(int[] arr, int k) {
        return f(arr,0,k,new Integer[arr.length]);
    }
    
    public int f(int[] a,int i,int k,Integer[] dp) {
        if(i>=a.length) return 0;
        if(dp[i]!=null) return dp[i];
        int ans=0;
        int val=0;
        int max=0;
        for(int j=i,l=1;j<a.length && l<=k;j++,l++) {
            int f1 = f(a,j+1,k,dp);
            val++;
            max=Math.max(max,a[j]);
            ans=Math.max(ans,f1+(val*max));
        }
        return dp[i]=ans;
    }
}