class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return nums[0] if nums[0] < nums[1] else nums[1]
        start, end = 0, len(nums) - 1
        if nums[start] < nums[end]:
            return nums[0]
        while start <= end:
            mid = start + (end - start) // 2
            if mid < end and nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif mid > start and nums[mid-1] > nums[mid]:
                return nums[mid]
            
            if nums[start] == nums[mid] and nums[mid] == nums[end]:
                if nums[start] > nums[start+1]:
                    return nums[start+1]
                start += 1
                if nums[end - 1] > nums[end]:
                    return nums[end]
                end -= 1
            elif nums[start] < nums[mid] or (nums[start] == nums[mid] and nums[mid] > nums[end]):
                start = mid + 1
            else:
                end = mid -1
        return nums[0]
