class Solution {
    public int numSquares(int n) {
        return f(n, new Integer[n + 5]);
    }

    public int f(int v, Integer[] dp) {
        if (v == 0)
            return 0;
        if (dp[v] != null)
            return dp[v];
        int ans = Integer.MAX_VALUE;
        for (int i = 1; i * i <= v; i++) {
            int f1 = f(v - (i * i), dp);
            ans = Math.min(ans, f1 + 1);
        }
        return dp[v] = ans;
    }
}