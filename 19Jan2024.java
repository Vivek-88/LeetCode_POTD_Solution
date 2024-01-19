// Problem Link :- https://leetcode.com/problems/minimum-falling-path-sum/

class Solution {
    public int minFallingPathSum(int[][] mat) {
        int n = mat.length, m = mat[0].length;
        int[][] dp = new int[n + 5][m + 5];

        int ans = Integer.MAX_VALUE;
        for (int i = n - 1; i >= 0; i--) {
            for (int j = 0; j < m; j++) {
                dp[i][j] = dp[i + 1][j];
                if (isValid(i + 1, j - 1, n, m))
                    dp[i][j] = Math.min(dp[i + 1][j - 1], dp[i][j]);
                if (isValid(i + 1, j + 1, n, m))
                    dp[i][j] = Math.min(dp[i + 1][j + 1], dp[i][j]);
                System.out.println(i + " " + j + " " + dp[i][j]);
                dp[i][j] += mat[i][j];
                // System.out.println(i+" "+j+" "+dp[i][j]);
                if (i == 0)
                    ans = Math.min(ans, dp[i][j]);
            }
        }
        return ans;
    }

    public boolean isValid(int i, int j, int n, int m) {
        return (j >= 0 && j < m && i >= 0 && i < n);
    }
}