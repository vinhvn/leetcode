class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        averages = set()
        while l < r:
            avg = (nums[l] + nums[r]) / 2
            averages.add(avg)
            l += 1
            r -= 1
        
        return len(averages)
    