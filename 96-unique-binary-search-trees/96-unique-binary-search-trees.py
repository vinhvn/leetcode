class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 0:
            return 0
        return self.unique_binary_search_trees_helper({}, 1, n)
    
    def unique_binary_search_trees_helper(self, hashmap: Dict, start: int, end: int) -> int:
        if start > end:
            return 1
        if end-start in hashmap:
            return hashmap[end-start]
        res = 0
        for i in range(start, end + 1):
            # i is the root of the tree
            left = self.unique_binary_search_trees_helper(hashmap, start, i - 1)
            right = self.unique_binary_search_trees_helper(hashmap, i + 1, end)
            res += left * right
        hashmap[end-start] = res
        return res
