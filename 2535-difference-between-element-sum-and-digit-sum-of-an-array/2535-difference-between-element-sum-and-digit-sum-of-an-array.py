class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elementSum = 0
        digitSum = 0
        for n in nums:
            elementSum += n
            while n:
                digitSum += n % 10
                n //= 10
        return abs(elementSum - digitSum)