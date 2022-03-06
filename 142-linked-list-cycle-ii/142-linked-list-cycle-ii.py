# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def find_length(target):
            p = target
            count = 0
            while p is not None:
                p = p.next
                count += 1
                if p == target:
                    return count
            return 0

        def find_cycle(target):
            slow, fast = target, target
            while (fast is not None and fast.next is not None):
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return slow
            return None

        slow, fast = head, head
        cycle = find_cycle(slow)
        if cycle is None:
            return None
        n = find_length(cycle)
        for i in range(n):
            fast = fast.next

        while slow is not fast:
            slow = slow.next
            fast = fast.next
        return slow
