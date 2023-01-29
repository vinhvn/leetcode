# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = None
        node = head
        while node:
            # skip if val is not target
            if node.val != val:
                prev = node
                node = node.next
                continue

            # val is target, check if head
            if head == node:
                head = head.next
            else:
                prev.next = node.next

            node = node.next
        
        return head