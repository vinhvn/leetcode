# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        prev = None
        node = head
        next = head
        
        while (node != None):
            next = node.next
            node.next = prev
            prev = node
            node = next

        return prev
