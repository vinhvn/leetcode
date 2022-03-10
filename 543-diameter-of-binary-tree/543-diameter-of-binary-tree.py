# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maximum = 0
        
        def dfs(node):
            nonlocal maximum
            if not node:
                return 0
            
            leftTree = dfs(node.left)
            rightTree = dfs(node.right)

            diameter = leftTree + rightTree
            maximum = max(maximum, diameter)
            
            return max(leftTree, rightTree) + 1

        dfs(root)
        return maximum
