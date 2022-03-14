class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutations = [[]]
        for num in nums:
            # take all existing permutations and add num to create new ones
            n = len(permutations)
            for _ in range(n):
                oldPermutation = permutations.pop(0)
                # create new permutations by adding num at every position
                for i in range(len(oldPermutation) + 1):
                    newPermutation = list(oldPermutation)  # make a copy
                    newPermutation.insert(i, num)
                    if len(newPermutation) < len(nums):
                        permutations.append(newPermutation)
                        continue
                    # add to results when fully built
                    res.append(newPermutation)

        return res
