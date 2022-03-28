class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for i in range(len(nums))]
        
        for i in range(1, len(nums)):
            output[i] = nums[i-1] * output[i-1]
        
        right_product = 1
        for i in range(len(nums) - 2, -1, -1):
            output[i] *= nums[i+1] * right_product
            right_product *= nums[i+1]

        return output
