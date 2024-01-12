/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {
    public int maxAncestorDiff(TreeNode root) {
        return f(root)[0];
    }

    public int[] f(TreeNode root) {
        if (root == null)
            return new int[] { 0, Integer.MAX_VALUE, Integer.MIN_VALUE };

        int[] f1 = f(root.left);
        int[] f2 = f(root.right);
        int[] ans = { 0, root.val, root.val };

        ans[1] = Math.min(ans[1], Math.min(f1[1], f2[1]));
        ans[2] = Math.max(ans[2], Math.max(f1[2], f2[2]));

        ans[0] = Math.max(Math.abs(ans[1] - root.val), Math.abs(ans[2] - root.val));
        ans[0] = Math.max(ans[0], Math.max(f1[0], f2[0]));
        return ans;
    }
}