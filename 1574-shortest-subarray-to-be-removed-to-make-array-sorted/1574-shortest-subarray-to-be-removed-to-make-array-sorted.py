class Solution:
    def findLengthOfShortestSubarray(self, nums: List[int]) -> int:
        l, r  = 0, len(nums) - 1
        while l < len(nums) - 1 and nums[l] <= nums[l+1]:
            l += 1
        
        if l == len(nums) - 1:
            return 0
        
        while r > 0 and nums[r-1] <= nums[r]:
            r -= 1
        
        output = min(len(nums) - l - 1, r)
        i1 = 0
        i2 = r
        while i1 <= l and i2 < len(nums):
            if nums[i1] <= nums[i2]:
                output = min(output, i2-i1-1)
                i1 += 1
            else:
                i2 += 1

        return output
