# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def findLen(node : TreeNode) :
            list = [0]*2
            # print(node.val,list)
            if node.left==None and node.right==None :
                return list
            
            elif node.left==None :
                l1 = findLen(node.right)
                list[0]=l1[0]+1
                list[1]=max(l1[0]+1,l1[1]);
            elif node.right==None :
                l1 = findLen(node.left)
                list[0]=l1[0]+1
                list[1]=max(l1[0]+1,l1[1]);
            
            else :
                l1 = findLen(node.left)
                l2 = findLen(node.right)
                list[0]=max(l1[0],l2[0])+1
                list[1]=max(l1[1],l2[1],l1[0]+l2[0]+2)
            
            return list
        return findLen(root)[1]