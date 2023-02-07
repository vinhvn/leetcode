class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Count = collections.Counter(nums1)
        nums2Count = collections.Counter(nums2)
        
        res = []
        for n in nums1Count:
            if n in nums2Count:
                res = res + [n] * min(nums1Count[n], nums2Count[n])
        
        return res