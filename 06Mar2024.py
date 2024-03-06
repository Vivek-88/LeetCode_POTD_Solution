# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(head==None) :
            return False
        l1 = head
        l2 = head.next
        while(l1!=None and l2!=None and l2.next!=None) :
            if(l1==l2) :
                return True
            l1 = l1.next
            l2 = l2.next.next
            
        return False