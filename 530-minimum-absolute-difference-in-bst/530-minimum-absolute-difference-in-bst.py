# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def traverse(node: Optional[TreeNode], vals: List[int]) -> List[int]:
            if not node:
                return vals
            
            traverse(node.left, vals)
            vals.append(node.val)
            traverse(node.right, vals)

            return vals
        
        vals = traverse(root, [])
        minDiff = math.inf
        for i in range(1, len(vals)):
            minDiff = min(minDiff, abs(vals[i] - vals[i-1]))
        
        return minDiff