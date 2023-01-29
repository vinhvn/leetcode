class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numIndexMap = defaultdict(int)
        
        for i, num in enumerate(nums):
            if num in numIndexMap and abs(i - numIndexMap[num]) <= k:
                return True
            numIndexMap[num] = i
        
        return False