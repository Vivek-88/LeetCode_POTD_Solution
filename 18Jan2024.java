// Problem Link :- https://leetcode.com/problems/climbing-stairs/

class Solution {
    public int climbStairs(int n) {
        int[] ans = new int[n + 5];
        ans[n] = 1;
        for (int i = n - 1; i >= 0; i--) {
            ans[i] = ans[i + 1] + ans[i + 2];
        }
        return ans[0];
    }
}