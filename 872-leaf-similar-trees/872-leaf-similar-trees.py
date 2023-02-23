# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeafValueSequence(node: Optional[TreeNode]) -> List[int]:
            if not node:
                return []
            
            if not node.left and not node.right:
                return [node.val]
            
            return getLeafValueSequence(node.left) + getLeafValueSequence(node.right)
        
        root1LeafSeq = getLeafValueSequence(root1)
        root2LeafSeq = getLeafValueSequence(root2)
        
        return root1LeafSeq == root2LeafSeq