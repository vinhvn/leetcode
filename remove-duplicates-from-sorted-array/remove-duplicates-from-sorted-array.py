class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        iterate through nums
        check adjacent nums to see if they match
        remove matching nums and continue iterating
        """
        i = 0
        while i < len(nums):
            if i != len(nums) - 1 and nums[i] == nums[i+1]:
                nums.pop(i+1)
            else:
                i += 1
        
        return len(nums)
        
        """
        n = len(nums)
        Time complexity: O(n), linear time. The loop will iterate over each number in nums once at most.
        Space complexity: O(1), constant space. The only variable used is to track index position.
        """