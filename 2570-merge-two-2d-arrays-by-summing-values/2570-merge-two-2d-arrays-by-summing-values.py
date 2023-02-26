class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:

        i1, i2 = 0, 0
        res = []
        while i1 < len(nums1) or i2 < len(nums2):
            if i1 == len(nums1):
                res.append(nums2[i2])
                i2 += 1
            elif i2 == len(nums2):
                res.append(nums1[i1])
                i1 += 1
            else:
                id1, val1 = nums1[i1]
                id2, val2 = nums2[i2]
                if id1 == id2:
                    res.append([id1, val1 + val2])
                    i1 += 1
                    i2 += 1
                elif id1 < id2:
                    res.append(nums1[i1])
                    i1 += 1
                else:
                    res.append(nums2[i2])
                    i2 += 1
        
        return res
    