class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            # check if num is greater than its neighbors
            if (
                (mid == 0 and nums[mid] > nums[mid + 1])
                or (mid == len(nums) - 1 and nums[mid - 1] < nums[mid])
                or (nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1])
            ):
                return mid
            # check if num is ascending or descending
            if mid != len(nums) - 1 and nums[mid] < nums[mid + 1]:
                start = mid + 1
            else:
                end = mid - 1
        return -1
