// Problem Link :- https://leetcode.com/problems/out-of-boundary-paths/

class Solution {
    public int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        return f(m, n, startRow, startColumn, maxMove, new Integer[m][n][maxMove + 1]);
    }

    public int f(int m, int n, int i, int j, int step, Integer[][][] dp) {
        if (step < 0)
            return 0;
        if (i < 0 || i >= m || j < 0 || j >= n)
            return 1;

        if (dp[i][j][step] != null)
            return dp[i][j][step];
        int f1 = f(m, n, i + 1, j, step - 1, dp);
        int f2 = f(m, n, i, j + 1, step - 1, dp);
        int f3 = f(m, n, i - 1, j, step - 1, dp);
        int f4 = f(m, n, i, j - 1, step - 1, dp);
        return dp[i][j][step] = add(add(f1, f2), add(f3, f4));
    }

    public int mod = 1000000007;

    public int add(int a, int b) {
        return (a + b) % mod;
    }
}