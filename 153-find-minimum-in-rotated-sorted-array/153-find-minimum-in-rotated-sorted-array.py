class Solution:
    def findMin(self, nums: List[int]) -> int:
        # base cases
        # 1 elem array or arr in sorted order (no rotations)
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            # return point of rotation if found
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            elif nums[mid] > nums[mid+1]:
                return nums[mid+1]

            # otherwise, do some binary search
            if nums[mid] > nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
