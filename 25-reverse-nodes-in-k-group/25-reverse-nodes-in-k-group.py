# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_length(head):
            count = 0
            while head is not None:
                head = head.next
                count += 1
            return count

        curr, prev = head, None
        length = get_length(head)
        while curr is not None:
            length -= k
            if length < 0:
                break
            beforeReverse = prev
            lastNode = curr
            # reverse k nodes
            i = 0
            while curr is not None and i < k:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                i += 1
            # connect with first node and last node
            if beforeReverse is not None:
                beforeReverse.next = prev
            else:
                head = prev
            lastNode.next = curr
            prev = lastNode

        return head
