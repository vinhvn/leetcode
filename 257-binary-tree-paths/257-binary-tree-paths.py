# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        def traverse(node: Optional[TreeNode], path: str):
            nonlocal paths
            
            if not node:
                return
            elif not node.left and not node.right:
                paths.append(f"{path}{node.val}")
            else:
                newPath = f"{path}{node.val}->"
                traverse(node.left, newPath)
                traverse(node.right, newPath)
        
        traverse(root, "")
        return paths
