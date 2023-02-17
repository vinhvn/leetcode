class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(n) for n in list(functools.reduce(lambda x,y: x + y, [str(n) for n in nums]))]