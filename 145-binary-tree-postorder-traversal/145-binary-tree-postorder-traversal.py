# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorderTraverse(root: Optional[TreeNode]) -> List[int]:
            def helper(node: Optional[TreeNode], path: List[int]) -> None:
                if not node:
                    return
                
                helper(node.left, path)
                helper(node.right, path)
                path.append(node.val)
            
            path = []
            helper(root, path)
            return path
        
        return postorderTraverse(root)