class Solution:
    def searchRange(self, nums: List[int], key: int) -> List[int]:
        # modified search to continue past finding the key
        def binary_search(start, end, findStart):
            if start > end:
                return -1
            mid = start + (end - start) // 2
            if key == nums[mid]:
                if findStart:
                    if mid == 0 or (mid > 0 and key != nums[mid - 1]):
                        return mid
                    return binary_search(start, mid - 1, findStart)
                else:
                    if mid == len(nums) - 1 or (
                        mid < len(nums) - 1 and key != nums[mid + 1]
                    ):
                        return mid
                    return binary_search(mid + 1, end, findStart)
            elif key < nums[mid]:
                return binary_search(start, mid - 1, findStart)
            else:
                return binary_search(mid + 1, end, findStart)
        # base case
        if len(nums) < 1:
            return [-1, -1]
        # find start
        start = binary_search(0, len(nums) - 1, True)
        if start == -1:  # if not found, return -1
            return [-1, -1]
        # find end
        end = binary_search(0, len(nums) - 1, False)
        return [start, end]
