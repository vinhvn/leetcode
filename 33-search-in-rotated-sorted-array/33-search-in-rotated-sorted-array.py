class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # subroutine to find minimum (LC 153)
        def findMinimum():
            # base cases
            # 1 elem array or arr in sorted order (no rotations)
            if len(nums) == 1 or nums[0] < nums[-1]:
                return 0

            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2

                # return point of rotation if found
                if nums[mid-1] > nums[mid]:
                    return mid
                elif nums[mid] > nums[mid+1]:
                    return mid+1

                # otherwise, do some binary search
                if nums[mid] > nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1
        
        # base case
        if len(nums) == 0:
            return -1
        # find minimum
        minIdx = findMinimum()
        
        # change left and right pointers based on minimum point
        left, right = 0, len(nums) - 1
        if nums[minIdx] <= target and target <= nums[right]:
            left = minIdx
        else:
            right = minIdx
        
        # binary search to find target
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid+1
            else:
                right = mid-1
        
        return -1
