class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        l, r = 0, len(nums)-1
        while l < r:
            mid = l + (r-l) // 2
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
        
        min = l
        l, r = 0, len(nums)-1
        if nums[min] <= target and target <= nums[r]:
            l = min
        else:
            r = min

        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid+1
            else:
                r = mid-1
        
        return -1
