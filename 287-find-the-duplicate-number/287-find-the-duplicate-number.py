class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        occurrences = [0 for i in range(len(nums) - 1)]
        for num in nums:
            if occurrences[num-1] == 1:
                return num
            occurrences[num-1] += 1
        return -1
