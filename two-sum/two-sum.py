class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            n = nums[i]
            if n in d:
                return [d[n], i]
            else:
                d[target - n] = i