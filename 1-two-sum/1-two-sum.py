class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetIndexMap = defaultdict(int)
        for i, num in enumerate(nums):
            if num in targetIndexMap:
                return [targetIndexMap[num], i]
            targetIndexMap[target - num] = i
        return [-1, -1]
