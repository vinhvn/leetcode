# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
            if not root1 and not root2:
                return True
            elif not root1 or not root2:
                return False
            
            return root1.val == root2.val and isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)
        
        def traverse(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            
            if node.val == subRoot.val and isSameTree(node, subRoot):
                return True
            
            return traverse(node.left) or traverse(node.right)
        
        return traverse(root)