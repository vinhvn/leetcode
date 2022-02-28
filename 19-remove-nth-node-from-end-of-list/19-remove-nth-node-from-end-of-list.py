# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def count(head):
            c = 0
            while head is not None:
                head = head.next
                c += 1
            return c
        
        def remove(head, i):
            prev = None
            while head is not None:
                if i == 0:
                    prev.next = head.next
                    return
                i -= 1
                prev = head
                head = head.next
        
        i = count(head) - n
        if i == 0:
            return head.next
        remove(head, i)
        return head