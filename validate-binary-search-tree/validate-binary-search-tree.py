# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nums = []
        def traverse(node: TreeNode) -> None:
            if not node:
                return
            traverse(node.left)
            nums.append(node.val)
            traverse(node.right)

        traverse(root)
        nums_sorted = sorted(nums)
        if len(nums) != len(set(nums_sorted)):
            return False
        for i in range(len(nums)):
            if nums[i] != nums_sorted[i]:
                return False
        return True