# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def getInOrderTraversal(node: Optional[TreeNode]) -> List[int]:
            if not node:
                return []
            
            res = getInOrderTraversal(node.left) + [node.val] + getInOrderTraversal(node.right)
            return res
        
        def buildIncTree(values: List[int]) -> TreeNode:
            root = TreeNode(values[0])
            node = root
            for i in range(1, len(values)):
                node.right = TreeNode(values[i])
                node = node.right
            return root
        
        inOrder = getInOrderTraversal(root)
        newRoot = buildIncTree(inOrder)
        
        return newRoot