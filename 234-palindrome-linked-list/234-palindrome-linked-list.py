# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
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
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True
