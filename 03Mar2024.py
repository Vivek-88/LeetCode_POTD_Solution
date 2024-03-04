# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from tkinter.tix import ListNoteBook
from pyparsing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNoteBook], n: int) -> Optional[ListNode]:
        list = []
        temp = head
        while head!=None :
            list.append(head)
            head=head.next
        if(n==len(list)) :
            temp=temp.next
        elif(n==1) :
            if(len(list)==1) :
                temp=None
            else :
                list[-2].next=None
        else :
            list[-n-1].next=list[-n+1]
        return temp