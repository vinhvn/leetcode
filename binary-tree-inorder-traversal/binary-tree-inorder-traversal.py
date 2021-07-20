# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        implement a recursive inorder traversal
        each will have lists of values that bubble up back to the top
        """
        def traverse(root: TreeNode) -> List[int]:
            if root == None:
                return []
            out = []
            out.extend(traverse(root.left))
            out.append(root.val)
            out.extend(traverse(root.right))
            return out
        
        return traverse(root)
        
        """
        n = num of nodes in tree
        Time complexity: O(n), linear time.
            Will traverse all nodes at least once.
        Space complexity: O(n), linear space.
            Stack size may grow up to n in length on poorly balanced trees.
        """