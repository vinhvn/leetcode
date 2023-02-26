class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set()
        res = -1
        for n in nums:
            if -n in seen:
                res = max(res, -n, n)
            seen.add(n)
        
        return res
    