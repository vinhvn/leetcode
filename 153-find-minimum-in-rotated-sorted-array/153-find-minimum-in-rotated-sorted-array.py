class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        
        # modified binary search to find point of rotation
        def binary_search(l, r):
            if l > r:
                return -1
            # midpoint
            mid = (l + r) // 2
            # return point of rotation if found
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid+1] < nums[mid]:
                return nums[mid+1]
            # otherwise, recurse on half
            elif nums[mid] > nums[l]:
                return binary_search(mid, r)
            return binary_search(l, mid)
        
        # if only 1 element or already sorted, return min
        if n == 1 or nums[n-1] > nums[0]:
            return nums[0]
        # else, run binary search
        return binary_search(0, n-1)