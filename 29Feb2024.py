# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        dq = deque()
        dq.append(root)
        level=0
        while(len(dq)>0) :
            l = len(dq)
            pv = inf
            if(level%2==0) :
                pv=0
            for _ in range(l) :
                n = dq.popleft()
                
                if(n==None) :
                    continue
                # print(n.val)
                if(n.val%2==level%2) :
                    return False
                if(level%2==0) :
                    if(pv>=n.val) :
                        return False
                else :
                    if(pv<=n.val) :
                        return False
                pv=n.val
                dq.append(n.left)
                dq.append(n.right)
            level+=1
        return True