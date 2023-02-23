# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def traverse(node: Optional[TreeNode], rootVal: int) -> bool:
            if not node:
                return True
            
            if node.val != rootVal:
                return False
            
            return traverse(node.left, rootVal) and traverse(node.right, rootVal)
        
        return traverse(root, root.val)