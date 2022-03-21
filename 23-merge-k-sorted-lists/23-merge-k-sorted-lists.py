# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
import random

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        minHeap = []  # k in size
        # add all list heads to the min heap
        for i in range(k):  # use index to differ duplicate values
            if lists[i] is not None:
                heapq.heappush(minHeap, (lists[i].val, i, lists[i].next))

        resultHead = None
        while minHeap:
            val, i, nextHead = heapq.heappop(minHeap)
            # if head is none, set the head
            if resultHead is None:
                resultHead = ListNode(val)
                node = resultHead
            else:  # otherwise, build the list nodes
                node.next = ListNode(val)
                node = node.next
            # if next is not None, add it back onto the heap
            if nextHead:
                heapq.heappush(minHeap, (nextHead.val, i, nextHead.next))

        return resultHead
