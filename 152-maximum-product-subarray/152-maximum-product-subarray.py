class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        final = nums[0]
        max_prod, min_prod = 1, 1
        for num in nums:
            temp = max_prod
            max_prod = max(num, max_prod * num, min_prod * num)
            min_prod = min(num, temp * num, min_prod * num)
            final = max(final, max_prod)
        return final
