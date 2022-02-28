# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
    
        slow, fast = head, head
        # move fast pointer n+1 times forward
        while n >= 0:
            n -= 1
            if fast is None:
                return head.next
            fast = fast.next
        
        # traverse until fast hits end of list
        while fast is not None:
            slow = slow.next
            fast = fast.next
        
        # remove next node
        slow.next = slow.next.next
        
        return head