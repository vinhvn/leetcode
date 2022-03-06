class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        next_non_val = 0
        for i, num in enumerate(nums):
            if num == val:
                continue
            nums[next_non_val] = num
            next_non_val += 1
        return next_non_val
