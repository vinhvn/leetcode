class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        # check all incorrect nums
        dupes = []
        for k in range(len(nums)):
            if nums[k] != k+1:
                dupes.append(nums[k])
        return dupes
