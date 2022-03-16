class Solution:
    def searchInsert(self, nums: List[int], key: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if key == nums[mid]:
                return mid
            elif key < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        # since loop runs until start <= end, at the end of while loop, start == end+1
        if start == len(nums) or start == 0:
            return start
        elif key < nums[start]:
            return start
        else:
            return end
