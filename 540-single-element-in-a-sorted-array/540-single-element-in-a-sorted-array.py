class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        start, end = 0, len(nums) -1
        while start <= end:
            mid = start + (end - start) // 2
            # check ends or num is not equal to its neighbors
            if (mid == 0 and nums[mid] != nums[mid+1]) or (mid == len(nums) - 1 and nums[mid-1] != nums[mid]) or (nums[mid-1] != nums[mid] and nums[mid] != nums[mid+1]):
                return nums[mid]
            # check what side the duplicate is on
            if mid % 2 == 0: # on an even index
                # dupe should be to its right
                if nums[mid] == nums[mid+1]:
                    start = mid + 1
                # dupe is not where it should be
                # single element must be displacing it
                else:
                    end = mid - 1
            else: # on an odd index
                # dupe should be to its left
                if nums[mid-1] == nums[mid]:
                    start = mid + 1
                else:
                    end = mid -1
        return start
