import java.util.Arrays;
import java.util.HashSet;
import java.util.Stack;

class Solution {
    public int evalRPN(String[] tokens) {
        Stack<String> stk = new Stack<>();
        HashSet<String> set = new HashSet<>(Arrays.asList(new String[] { "+", "-", "*", "/" }));
        // System.out.println(set);
        for (String t : tokens) {
            if (set.contains(t)) {
                int a = Integer.parseInt(stk.pop());
                int b = Integer.parseInt(stk.pop());
                stk.push(f(b, a, t.charAt(0)) + "");
            } else {
                stk.push(t);
            }
            // System.out.println(stk);
        }
        // System.out.println(stk);
        return Integer.parseInt(stk.pop());
    }

    public int f(int a, int b, char t) {
        if (t == '+') {
            return a + b;
        } else if (t == '-') {
            return a - b;
        } else if (t == '*') {
            return a * b;
        } else {
            return a / b;
        }
    }
}