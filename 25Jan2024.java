class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        return f(text1, text2, 0, 0, new Integer[text1.length()][text2.length()]);
    }

    public int f(String s1, String s2, int i, int j, Integer[][] dp) {
        if (i >= s1.length() || j >= s2.length())
            return 0;
        if (dp[i][j] != null)
            return dp[i][j];
        int f1 = f(s1, s2, i + 1, j, dp);
        int f2 = f(s1, s2, i, j + 1, dp);
        int ans = Math.max(f1, f2);
        if (s1.charAt(i) == s2.charAt(j)) {
            int f3 = f(s1, s2, i + 1, j + 1, dp);
            ans = Math.max(ans, f3 + 1);
        }
        return dp[i][j] = ans;
    }
}