# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def helper(node: Optional[TreeNode], high: int, low: int) -> int:
            if not node:
                return high - low
            
            leftDiff = helper(node.left, node.val, low)
            rightDiff = helper(node.right, high, node.val)
            
            return min(leftDiff, rightDiff)
        
        return helper(root, math.inf, -math.inf)