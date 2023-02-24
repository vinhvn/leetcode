# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def mergeTraverse(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node1 and not node2:
                return None
            
            newNode = TreeNode()
            if node1:
                newNode.val += node1.val
            if node2:
                newNode.val += node2.val
            
            newNode.left = mergeTraverse(node1.left if node1 else None, node2.left if node2 else None)
            newNode.right = mergeTraverse(node1.right if node1 else None, node2.right if node2 else None)

            return newNode
        
        return mergeTraverse(root1, root2)