"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def traverse(node: 'Node', path: List[int]) -> None:
            if not node:
                return
            
            for child in node.children:
                traverse(child, path)
            
            path.append(node.val)
        
        path = []
        traverse(root, path)
        return path