class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        
        def binary_search(l, r):
            if l > r:
                return -1
            
            mid = (l + r) // 2
            
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid+1] < nums[mid]:
                return nums[mid+1]

            elif nums[mid] > nums[l]:
                return binary_search(mid, r)
            else:
                return binary_search(l, mid)
        
        if n == 1 or nums[n-1] > nums[0]:
            return nums[0]
        return binary_search(0, n-1)