// Problem Link :- https://leetcode.com/problems/house-robber/

class Solution {
    public int rob(int[] nums) {
        return f(nums, 0, 0, new Integer[nums.length][2]);
    }

    public int f(int[] a, int i, int j, Integer[][] dp) {
        if (i >= a.length)
            return 0;

        if (dp[i][j] != null)
            return dp[i][j];
        int f1 = f(a, i + 1, 0, dp);
        int ans = f1;
        if (j == 0) {
            int f2 = f(a, i + 1, 1, dp) + a[i];
            ans = Math.max(ans, f2);
        }
        return dp[i][j] = ans;
    }
}