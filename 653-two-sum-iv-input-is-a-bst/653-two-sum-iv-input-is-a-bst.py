# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def helper(node: Optional[TreeNode], targets: Set[int]) -> bool:
            if not node:
                return False
            
            if node.val in targets:
                return True
            
            targets.add(k - node.val)
            return helper(node.left, targets) or helper(node.right, targets)
        
        return helper(root, set())