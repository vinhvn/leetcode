class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for num in nums:
            # take all existing subsets and insert num to create new subsets
            size = len(subsets)
            for i in range(size):
                # create copy of subset and add current number into it
                copy = list(subsets[i])
                copy.append(num)
                subsets.append(copy)

        return subsets
