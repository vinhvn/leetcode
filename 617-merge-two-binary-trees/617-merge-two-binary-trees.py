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
            
            if node1 and node2:
                newNode.left = mergeTraverse(node1.left, node2.left)
                newNode.right = mergeTraverse(node1.right, node2.right)
            elif node1:
                newNode.left = mergeTraverse(node1.left, None)
                newNode.right = mergeTraverse(node1.right, None)
            else:
                newNode.left = mergeTraverse(None, node2.left)
                newNode.right = mergeTraverse(None, node2.right)
                
            return newNode
        
        return mergeTraverse(root1, root2)