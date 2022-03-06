class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        subarrays = start = 0
        product = 1
        for end in range(len(nums)):
            product *= nums[end]
            while product >= k and end >= start:
                product /= nums[start]
                start += 1
            subarrays += end - start + 1
        return subarrays
