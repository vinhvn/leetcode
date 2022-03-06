class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        occurrences = [0 for i in range(len(nums))]
        dupes = []
        for num in nums:
            if occurrences[num-1] == 1:
                dupes.append(num)
            occurrences[num-1] += 1
        return dupes
