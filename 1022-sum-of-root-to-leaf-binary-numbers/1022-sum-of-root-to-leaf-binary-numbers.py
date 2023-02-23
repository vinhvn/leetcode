# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def helper(node: Optional[TreeNode], path: List[str]) -> int:
            if not node:
                return 0
            
            path.append(str(node.val))
            
            if not node.left and not node.right:
                res = int("".join(path), 2)
                path.pop()
                return res
            
            res = helper(node.left, path) + helper(node.right, path)
            path.pop()
            return res
        
        return helper(root, [])