"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def traverse(node: 'Node', path: List[int]) -> None:
            if not node:
                return
            
            path.append(node.val)

            if not node.children:
                return

            for child in node.children:
                traverse(child, path)
        
        path = []
        traverse(root, path)
        return path