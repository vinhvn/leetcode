class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_to_right = [1 for i in range(len(nums))]
        right_to_left = [1 for i in range(len(nums))]
        
        for i in range(1, len(nums)):
            left_to_right[i] = nums[i-1] * left_to_right[i-1]
        
        for i in range(len(nums) - 2, -1, -1):
            right_to_left[i] = nums[i+1] * right_to_left[i+1]
        
        return [left_to_right[i] * right_to_left[i] for i in range(len(nums))]