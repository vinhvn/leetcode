# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
import random

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def llpop(head):
            if not head:
                return None
            return (head.val, random.getrandbits(128), head.next)

        if len(lists) == 0:
            return None
        
        heap = []
        k = len(lists)
        # add one element from each list to heap
        for i in range(k):
            if lists[i] is not None:
                heapq.heappush(heap, llpop(lists[i]))

        if len(heap) == 0:
            return None

        # build list
        head = ListNode()
        prev = None
        node = head
        while len(heap) > 0:
            popped = heapq.heappop(heap)
            if popped[2] is not None:
                heapq.heappush(heap, llpop(popped[2]))
            node.val = popped[0]
            node.next = ListNode()
            prev = node
            node = node.next
        if prev is not None:
            prev.next = None
        return head
