class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        # check all incorrect nums
        missing = []
        for j in range(len(nums)):
            if nums[j] != j+1:
                missing.append(j+1)
        return missing
