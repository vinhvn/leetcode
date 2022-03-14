# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n <= 0:
            return 0
        return self.unique_binary_search_trees_helper(1, n)

    def unique_binary_search_trees_helper(self, start: int, end: int) -> List[TreeNode]:
        if start > end:
            return [None]
        res = []
        for i in range(start, end + 1):
            # i is the root of the tree
            leftSubtrees = self.unique_binary_search_trees_helper(start, i - 1)
            rightSubtrees = self.unique_binary_search_trees_helper(i + 1, end)
            for left in leftSubtrees:
                for right in rightSubtrees:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    res.append(root)

        return res
