# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        def dfs(node, curSum, curPath):
            if not node:
                return
            curSum += node.val
            path = list(curPath)
            path.append(node.val)
            if curSum == targetSum and not node.left and not node.right:
                paths.append(path)
                return
            
            dfs(node.left, curSum, path)
            dfs(node.right, curSum, path)
        
        dfs(root, 0, [])
        return paths
