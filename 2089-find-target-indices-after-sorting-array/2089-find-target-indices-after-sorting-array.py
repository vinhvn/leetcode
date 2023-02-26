class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        def getFirstIndex(nums: List[int], target: int) -> int:
            res = -1
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] >= target:
                    res = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return res
        
        def getLastIndex(nums: List[int], target: int) -> int:
            res = -1
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] <= target:
                    res = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return res

        nums.sort()
        firstIndex = getFirstIndex(nums, target)
        if firstIndex == -1:
            return []
        lastIndex = getLastIndex(nums, target)
        return range(firstIndex, lastIndex + 1)
