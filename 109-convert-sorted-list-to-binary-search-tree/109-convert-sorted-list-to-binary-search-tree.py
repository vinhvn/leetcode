# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def getListFromLinkedList(node: Optional[ListNode]) -> List[int]:
            if not node:
                return []
            
            return [node.val] + getListFromLinkedList(node.next)
        
        def buildBST(values: List[int], low: int, high: int) -> Optional[TreeNode]:
            if not values or low > high:
                return None
            
            mid = (low + high) // 2
            newNode = TreeNode(values[mid])
            newNode.left = buildBST(values, low, mid - 1)
            newNode.right = buildBST(values, mid + 1, high)

            return newNode
        
        vals = getListFromLinkedList(head)
        root = buildBST(vals, 0, len(vals) - 1)
        
        return root