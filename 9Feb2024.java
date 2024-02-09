import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<Integer> largestDivisibleSubset(int[] nums) {
        int n = nums.length;
        int maxi = 1;
        int num = -1;
        List<Integer> v = new ArrayList<>();
        Arrays.sort(nums);
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if ((nums[i] % nums[j]) == 0 && dp[i] < dp[j] + 1) {
                    dp[i] = dp[j] + 1;
                    if (maxi < dp[i]) {
                        maxi = dp[i];
                    }
                }
            }
        }
        for (int i = n - 1; i >= 0; i--) {
            if (maxi == dp[i] && (num == -1 || (num % nums[i]) == 0)) {
                v.add(nums[i]);
                maxi--;
                num = nums[i];
            }
        }
        return v;
    }
}