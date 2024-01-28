class Solution {
    public int numSubmatrixSumTarget(int[][] matrix, int target) {
        int n = matrix.length, m = matrix[0].length;
        int[][] dp = new int[n][m];
        for (int i = 0; i < n; i++) {
            int sum = 0;
            for (int j = 0; j < m; j++) {
                sum += matrix[i][j];
                dp[i][j] = sum;
                if (i != 0)
                    dp[i][j] += dp[i - 1][j];
            }
        }

        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                for (int k = i; k < n; k++) {
                    for (int l = j; l < m; l++) {
                        int val = dp[k][l];
                        if (j - 1 >= 0)
                            val -= dp[k][j - 1];
                        if (i - 1 >= 0)
                            val -= dp[i - 1][l];
                        if (j - 1 >= 0 && i - 1 >= 0)
                            val += dp[i - 1][j - 1];
                        if (val == target)
                            ans++;
                    }
                }
            }
        }
        return ans;
    }
}