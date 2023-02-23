# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque()
        q.append((root, -1))
        while q:
            lenLevel = len(q)
            xParent = yParent = None
            for i in range(lenLevel):
                node, parent = q.popleft()
                if node.val == x:
                    xParent = parent
                if node.val == y:
                    yParent = parent
                if xParent and yParent and xParent != yParent:
                    return True

                # add to q
                if node.left:
                    q.append((node.left, node.val))
                if node.right:
                    q.append((node.right, node.val))

            if xParent or yParent:
                return False
        
        return False