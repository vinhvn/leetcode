# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        values = []
        if root is None:
            return values
        
        queue = []
        queue.append(root)
        while queue:
            levelSize = len(queue)
            currentLevel = []
            for _ in range(levelSize):
                currentNode = queue.pop(0)
                # alternate between adding at end and front of lists based on level
                if len(values) % 2 == 0:
                    currentLevel.append(currentNode.val)
                else:
                    currentLevel.insert(0, currentNode.val)

                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            
            values.append(currentLevel)
        
        return values
