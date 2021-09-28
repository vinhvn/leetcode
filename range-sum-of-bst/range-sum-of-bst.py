# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def traverse(node: TreeNode) -> int:
            if not node:
                return 0
            val = node.val if node.val >= low and node.val <= high else 0
            return val + traverse(node.left) + traverse(node.right)
        
        return traverse(root)
