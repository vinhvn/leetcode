class Solution:
    def search(self, nums: List[int], key: int) -> bool:
        if len(nums) == 1:
            return nums[0] == key
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if key == nums[mid]:
                return True
            # shrink if all indices result in the same number
            if nums[start] == nums[mid] and nums[mid] == nums[end]:
                start += 1
                end -= 1
            # check if left side is in ascending order
            elif nums[start] <= nums[mid]:
                # check if key is within range
                if nums[start] <= key and key < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:  # right side is in ascending order
                if nums[mid] < key and key <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return False
