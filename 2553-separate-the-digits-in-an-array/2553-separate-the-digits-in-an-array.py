class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        combined = functools.reduce(lambda x,y: x + y, [str(n) for n in nums])
        return [int(n) for n in list(combined)]