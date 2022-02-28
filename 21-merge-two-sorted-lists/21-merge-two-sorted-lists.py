# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        
        # build new list
        head = ListNode()
        prev = None
        node = head
        n1, n2 = list1, list2
        while n1 is not None and n2 is not None:
            if n1.val < n2.val:
                node.val = n1.val
                n1 = n1.next
            else:
                node.val = n2.val
                n2 = n2.next
            node.next = ListNode()
            prev = node
            node = node.next
        while n1 is not None:
            node.val = n1.val
            n1 = n1.next
            node.next = ListNode()
            prev = node
            node = node.next
        while n2 is not None:
            node.val = n2.val
            n2 = n2.next
            node.next = ListNode()
            prev = node
            node = node.next
        prev.next = None
        return head
