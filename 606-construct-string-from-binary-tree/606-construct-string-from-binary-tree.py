# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def traverse(node: Optional[TreeNode], res: List[str]) -> None:
            if not node:
                return
            
            res.append(str(node.val))
            if node.left:
                res.append("(")
                traverse(node.left, res)
                res.append(")")
            if node.right:
                if not node.left:
                    res.append("()")
                res.append("(")
                traverse(node.right, res)
                res.append(")")
        
        res = []
        traverse(root, res)
        return "".join(res)