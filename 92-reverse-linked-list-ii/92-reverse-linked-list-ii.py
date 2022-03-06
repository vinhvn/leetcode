# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], p: int, q: int) -> Optional[ListNode]:
        if p == q:
            return head
        # skip p-1 nodes, current will point at node p
        curr, prev = head, None
        i = 0
        while curr is not None and i < p-1:
            prev = curr
            curr = curr.next
            i += 1
        # store node at p-1 and node at p (will be q after reversal)
        beforeP = prev
        nodeQ = curr
        # reverse nodes between p and q
        i = 0
        while curr is not None and i < (q-p+1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            i += 1
        # connect with first node and last node
        if beforeP is not None:
            beforeP.next = prev
        else:
            head = prev
        nodeQ.next = curr

        return head
