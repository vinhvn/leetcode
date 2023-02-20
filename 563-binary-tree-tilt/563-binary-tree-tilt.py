# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        sumTilt = 0

        def traverse(node: Optional[TreeNode]) -> int:
            nonlocal sumTilt
            if not node:
                return
            
            leftVal = traverse(node.left) if node.left else 0
            rightVal = traverse(node.right) if node.right else 0
            sumTilt += abs(leftVal - rightVal)

            return node.val + leftVal + rightVal

        traverse(root)
        return sumTilt