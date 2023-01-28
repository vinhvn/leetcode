# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorderTraverse(node: Optional[TreeNode]) -> List[int]:
            def helper(node: Optional[TreeNode], path: List[int]) -> None:
                if not node:
                    return 
            
                path.append(node.val)
                helper(node.left, path)
                helper(node.right, path)

            path = []
            helper(node, path)
            return path

        return preorderTraverse(root)
