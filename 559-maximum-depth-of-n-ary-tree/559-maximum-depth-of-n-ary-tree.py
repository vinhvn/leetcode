"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def height(node: 'Node') -> int:
            if not node:
                return 0
            
            heights = [height(child) for child in node.children]
            
            return 1 + max(heights) if heights else 1

        return height(root)