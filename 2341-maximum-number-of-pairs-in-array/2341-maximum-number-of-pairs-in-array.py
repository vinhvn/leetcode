class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        numCount = collections.Counter(nums)
        pairs, leftover = 0, 0
        for v in numCount.values():
            pairs += v // 2
            leftover += v % 2
        
        return [pairs, leftover]
    