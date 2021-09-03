class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        subarrays = 0
        product = 1
        start = 0
        for end in range(len(nums)):
            product *= nums[end]
            while product >= k and start < len(nums):
                product /= nums[start]
                start += 1
            if start <= end:
                subarrays += end - start + 1
        return subarrays