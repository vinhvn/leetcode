class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len, ones, start = 0, 0, 0
        for end in range(len(nums)):
            if nums[end] == 1:
                ones += 1
            if end - start + 1 > ones + k:
                if nums[start] == 1:
                    ones -= 1
                start += 1
            max_len = max(max_len, end - start + 1)
        return max_len
