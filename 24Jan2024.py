# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    class Object :
        def __init__(self, fre, node=None):
            self.fre = fre
            self.node = node
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        dq = []
        dq.append(self.Object([0]*10,root))
        # print(len(dq))
        ans=0
        while(len(dq)>0) :
            lt = dq[-1]
            # print(lt.node)
            dq.pop()
            nd = lt.node
            fr = lt.fre
            if(nd==None) :
                continue
            fr[nd.val]+=1
            # print(nd.val)
            if(nd.left==None and nd.right==None) :
                o=0
                for f in fr :
                    if(f%2==1) :
                        o+=1
                if(o<=1) :
                    ans+=1
                # print(fr)
                continue
            dq.append(self.Object(fr.copy(),nd.left))
            dq.append(self.Object(fr.copy(),nd.right))
        # print(dq)
        return ans