class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = [[]]
        start = end = 0
        for i in range(len(nums)):
            start = 0
            if i > 0 and nums[i-1] == nums[i]:
                    start = end + 1
            end = len(subsets) - 1
            for j in range(start, end+1):
                copy = list(subsets[j])
                copy.append(nums[i])
                subsets.append(copy)

        return subsets
