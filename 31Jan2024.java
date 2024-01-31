import java.util.Stack;

class Solution {
    public int[] dailyTemperatures(int[] t) {
        Stack<Integer> stk = new Stack<>();
        int n = t.length;
        int[] ans = new int[n];
        for (int i = t.length - 1; i >= 0; i--) {
            while (stk.size() > 0 && t[stk.peek()] <= t[i])
                stk.pop();
            if (stk.size() == 0) {
                ans[i] = 0;
            } else {
                ans[i] = stk.peek() - i;
            }
            stk.push(i);
        }
        return ans;
    }
}