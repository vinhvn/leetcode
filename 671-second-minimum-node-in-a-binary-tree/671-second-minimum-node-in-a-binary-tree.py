# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        maxHeap = []
        visited = set()
        k = 2
        
        def traverse(node: Optional[TreeNode]) -> None:
            if not node:
                return
            
            nonlocal maxHeap, visited, k

            if node.val not in visited:
                visited.add(node.val)
                if len(maxHeap) < k:
                    heapq.heappush(maxHeap, -node.val)
                elif node.val < -maxHeap[0]:
                    heapq.heappushpop(maxHeap, -node.val)
            
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        return -maxHeap[0] if len(maxHeap) > 1 else -1
            
        