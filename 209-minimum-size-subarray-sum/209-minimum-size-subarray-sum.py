class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        smallest_size = len(nums) + 1 # max size
        cur_sum, start = 0, 0
        for end in range(len(nums)):
            cur_sum += nums[end]
            # shrink the window if the sum is too large
            while cur_sum >= target:
                smallest_size = min(smallest_size, end-start+1)
                cur_sum -= nums[start]
                start += 1
        return 0 if smallest_size == len(nums) + 1 else smallest_size