class Solution {
    public int[] rearrangeArray(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];
        for (int i = 0, j = 0, k = 0; i < n; i++) {
            if (i % 2 == 0) {
                while (j < n && nums[j] < 0)
                    j++;
                ans[i] = nums[j++];
            } else {
                while (k < n && nums[k] > 0)
                    k++;
                ans[i] = nums[k++];
            }
        }
        return ans;
    }
}