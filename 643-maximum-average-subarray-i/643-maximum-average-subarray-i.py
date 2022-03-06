class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float("-inf")
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if i >= k-1:
                max_avg = max(max_avg, curr_sum / k)
                curr_sum -= nums[i-k+1]
        return max_avg