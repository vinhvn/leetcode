# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightView = []
        if not root:
            return rightView
        
        queue = []
        queue.append(root)
        while queue:
            levelSize = len(queue)
            currentNode = None
            for _ in range(levelSize):
                currentNode = queue.pop(0)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            
            rightView.append(currentNode.val)
        
        return rightView
