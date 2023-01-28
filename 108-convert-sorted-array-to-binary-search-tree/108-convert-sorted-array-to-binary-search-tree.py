# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def mergeBST(arr) -> Optional[TreeNode]:
            if len(arr) == 0:
                return None
            elif len(arr) == 1:
                return TreeNode(arr[0], None, None)

            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid+1:]
            
            leftNode = mergeBST(left)
            rightNode = mergeBST(right)

            return TreeNode(arr[mid], leftNode, rightNode)

        return mergeBST(nums)
