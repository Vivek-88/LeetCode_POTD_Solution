# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l1 = head
        l2 = head
        while(l1!=None and l2!=None and l2.next!=None) :
            l1=l1.next
            l2=l2.next.next
        return l1