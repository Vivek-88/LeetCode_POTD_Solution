// Problem Link :- https://leetcode.com/problems/sum-of-subarray-minimums/

import java.util.Stack;

class Solution {
    public int sumSubarrayMins(int[] arr) {
        int n = arr.length;
        Stack<Integer> stk = new Stack<>();
        int[] left = new int[n];
        for (int i = 0; i < n; i++) {
            while (stk.size() > 0 && arr[i] < arr[stk.peek()])
                stk.pop();
            if (stk.size() == 0) {
                left[i] = -1;
            } else {
                left[i] = stk.peek();
            }
            stk.push(i);
        }
        stk = new Stack<>();
        int[] right = new int[n];
        for (int i = n - 1; i >= 0; i--) {
            while (stk.size() > 0 && arr[i] <= arr[stk.peek()])
                stk.pop();
            if (stk.size() == 0) {
                right[i] = n;
            } else {
                right[i] = stk.peek();
            }
            stk.push(i);
        }
        // a b c d e f g h i j k l
        System.out.println(Arrays.toString(left) + " " + Arrays.toString(right));

        int ans = 0;
        for (int i = 0; i < n; i++) {
            int val = multi(sub(right[i], i), sub(i, left[i]));
            // System.out.println(i+" "+val);
            val = multi(val, arr[i]);
            ans = add(ans, val);
        }
        return ans;
    }

    public final int mod = 1000000007;

    public int add(long a, long b) {
        return (int) (((a % mod) + (b % mod)) % mod);
    }

    public int sub(long a, long b) {
        return (int) (((a % mod) - (b % mod) + mod) % mod);
    }

    public int multi(long a, long b) {
        return (int) (((a % mod) * (b % mod)) % mod);
    }

}