# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def traverse(node: Optional[TreeNode], cameFromRight: bool) -> int:
            if not node:
                return 0
            
            if not node.left and not node.right and cameFromRight:
                return node.val
            
            return traverse(node.left, True) + traverse(node.right, False)
        
        return traverse(root, False)