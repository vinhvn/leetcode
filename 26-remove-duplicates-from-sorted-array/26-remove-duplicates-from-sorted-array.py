class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        next_non_dupe = 1
        for i in range(1, len(nums)):
            if nums[next_non_dupe - 1] != nums[i]:
                nums[next_non_dupe] = nums[i]
                next_non_dupe += 1
        return next_non_dupe