// Jai Shree Ram
// Problem Link :- https://leetcode.com/problems/set-mismatch/

import java.util.HashSet;

class Solution {
    public int[] findErrorNums(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        int[] ans = new int[2];
        for (int num : nums) {
            if (set.contains(num)) {
                ans[0] = num;
            }
            set.add(num);
        }

        for (int i = 1; i <= nums.length; i++) {
            if (!set.contains(i))
                ans[1] = i;
        }
        return ans;
    }
}