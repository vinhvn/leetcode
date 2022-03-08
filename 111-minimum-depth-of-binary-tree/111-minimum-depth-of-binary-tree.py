# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        minimum = 0
        if not root:
            return minimum
        
        queue = []
        queue.append(root)
        minimum = 1
        while queue:
            levelSize = len(queue)
            for _ in range(levelSize):
                currentNode = queue.pop(0)
                if not currentNode.left and not currentNode.right:
                    return minimum
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            
            minimum += 1
        
        return minimum
