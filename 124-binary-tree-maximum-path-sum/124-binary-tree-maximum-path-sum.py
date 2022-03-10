# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # store global max
        maximum = root.val

        def dfs(node):
            nonlocal maximum
            if not node:
                return 0

            # find sums of left and right subtrees
            leftSum = dfs(node.left)
            rightSum = dfs(node.right)

            # calculate current node's sum
            curSum = node.val + max(leftSum + rightSum, leftSum, rightSum, 0)
            # set global maximum
            maximum = max(maximum, curSum)

            # bubble up current node + max of the sums for any nodes above us
            return node.val + max(leftSum, rightSum, 0)

        dfs(root)
        return maximum
