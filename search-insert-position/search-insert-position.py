class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        use binary search to find target
        if found, return index
        else, return index where it would be placed
        """
        
        def binarySearch(low: int, high: int) -> int:
            if low > high:
                return low
            
            mid = (low + high) // 2
            
            if nums[mid] < target:
                return binarySearch(mid + 1, high)
            elif nums[mid] > target:
                return binarySearch(low, mid - 1)
            else:
                return mid
        
        return binarySearch(0, len(nums) - 1)
