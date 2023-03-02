class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        numCount = collections.Counter(nums)
        for v in numCount.values():
            if v % 2 == 1:
                return False
        
        return True
    