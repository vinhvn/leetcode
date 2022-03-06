class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        # swap
        while i < len(nums):
            j = nums[i]
            # can't fit [0..n] in array of length n
            if j < len(nums) and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        # iterate and find missing number
        for k in range(len(nums)):
            if nums[k] != k:
                return k
        return len(nums)
