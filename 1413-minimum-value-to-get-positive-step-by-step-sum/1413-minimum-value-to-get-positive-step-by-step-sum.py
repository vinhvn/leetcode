class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minSum = math.inf
        curSum = 0
        for num in nums:
            curSum += num
            minSum = min(minSum, curSum)
        return -minSum + 1 if minSum <= 0 else 1
