class Solution {
    public int countSubstrings(String s) {
        Integer[][] dp = new Integer[s.length()][s.length()];
        int ans = 0;
        for (int i = 0; i < s.length(); i++) {
            for (int j = i; j < s.length(); j++) {
                ans += f(s, i, j, dp);
            }
        }
        return ans;
    }

    public int f(String s, int i, int j, Integer[][] dp) {
        // System.out.println(i+" "+j);
        if (i >= j)
            return dp[i][j] = 1;
        if (dp[i][j] != null)
            return dp[i][j];
        int ans = 0;
        if (s.charAt(i) == s.charAt(j)) {
            ans += f(s, i + 1, j - 1, dp);
        }
        return dp[i][j] = ans;
    }
}