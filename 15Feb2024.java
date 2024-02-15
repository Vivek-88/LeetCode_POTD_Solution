import java.util.Arrays;

class Solution {
    public long largestPerimeter(int[] nums) {
        Arrays.sort(nums);
        long ans = -1, sum = nums[0] + nums[1];
        for (int i = 2; i < nums.length; i++) {
            if (nums[i] < sum) {
                ans = Math.max(ans, sum + (long) nums[i]);
            }
            sum += (long) (nums[i]);
        }
        return ans;

    }
}