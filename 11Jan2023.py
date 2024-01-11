# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.f(root)[0]

    def f(self, root: TreeNode) -> List[int]:
        if not root:
            return [0, float('inf'), float('-inf')]

        f1 = self.f(root.left)
        f2 = self.f(root.right)
        ans = [0, root.val, root.val]

        ans[1] = min(ans[1], min(f1[1], f2[1]))
        ans[2] = max(ans[2], max(f1[2], f2[2]))

        ans[0] = max(abs(ans[1] - root.val), abs(ans[2] - root.val))
        ans[0] = max(ans[0], max(f1[0], f2[0]))

        return ans