# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def getLengthList(head: ListNode) -> int:
            res = 0
            while head:
                head = head.next
                res += 1
            return res
        
        lenA = getLengthList(headA)
        lenB = getLengthList(headB)
        lenDiff = abs(lenA - lenB)
        
        if lenA < lenB:
            for _ in range(lenDiff):
                headB = headB.next
        elif lenB < lenA:
            for _ in range(lenDiff):
                headA = headA.next
        
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None