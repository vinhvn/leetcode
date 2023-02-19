# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def findModeHelper(node: Optional[TreeNode], counter: Dict[int, int]) -> Dict[int, int]:
            if not node:
                return counter
            
            counter[node.val] += 1
            
            findModeHelper(node.left, counter)
            findModeHelper(node.right, counter)

            return counter
        
        counter = findModeHelper(root, defaultdict(int))
        maxCount = max(counter.values())
        res = [k for k,v in counter.items() if v == maxCount]
        
        return res
        