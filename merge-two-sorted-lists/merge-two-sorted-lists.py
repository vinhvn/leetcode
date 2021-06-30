# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (l1 == None and l2 == None):
            return None
        
        head = ListNode()
        h0 = head
        
        h1 = l1
        h2 = l2
        
        while (h1 != None and h2 != None):
            if (h1.val <= h2.val):
                h0.val = h1.val
                h1 = h1.next
            else:
                h0.val = h2.val
                h2 = h2.next
            
            h0.next = ListNode()
            h0 = h0.next
        
        hextend = None
        if (h1 != None):
            hextend = h1
        else:
            hextend = h2
        
        while (hextend != None):
            h0.val = hextend.val
            if (hextend.next != None):
                h0.next = ListNode()
                h0 = h0.next
            hextend = hextend.next

        return head