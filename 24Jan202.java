import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.List;

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
    public int pseudoPalindromicPaths(TreeNode root) {
        ArrayDeque<List<Object>> dq = new ArrayDeque<>();
        int[] arr = new int[10];
        dq.add(Arrays.asList(new Object[] { root, arr }));
        int ans = 0;
        while (dq.size() > 0) {
            List<Object> list = dq.pop();
            TreeNode node = (TreeNode) list.get(0);
            int[] fre = (int[]) list.get(1);
            if (node == null)
                continue;
            fre[node.val]++;
            if (node.left == null && node.right == null) {
                int o = 0;
                for (int f : fre)
                    if (f % 2 == 1)
                        o++;
                if (o <= 1)
                    ans++;
                continue;
            }
            dq.add(Arrays.asList(new Object[] { node.left, fre.clone() }));
            dq.add(Arrays.asList(new Object[] { node.right, fre.clone() }));
        }
        return ans;
    }
}