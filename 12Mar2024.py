# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from pyparsing import Optional


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list = []
        ans=head
        while(head!=None) :
            list.append(head)
            sum=0
            idx=-1
            for i in range(len(list)-1,-1,-1) :
                sum+=list[i].val
                if(sum==0) :
                    idx=i
                    break
            if(idx!=-1) :
                for i in range(len(list),idx,-1) :
                    list.pop()
                if(len(list)==0) :
                    ans=head.next
                else :
                    list[-1].next=head.next
            head = head.next
        return ans