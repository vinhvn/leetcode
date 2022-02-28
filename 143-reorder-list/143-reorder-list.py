# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def get_middle_node(head):
            slow, fast = head, head
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def reverse(head):
            prev = None
            while head is not None:
                next = head.next
                head.next = prev
                prev = head
                head = next
            return prev
        
        rev_head = reverse(get_middle_node(head))
        p1 = head
        p2 = rev_head
        while p1 is not None and p2 is not None:
            p1_next = p1.next
            p1.next = p2
            p2_next = p2.next
            p2.next = p1_next
            p1 = p1_next
            p2 = p2_next
        
        if p1 is not None:
            p1.next = None
        
        return head