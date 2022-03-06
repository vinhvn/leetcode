class Solution:
    def intervalIntersection(self, a1: List[List[int]], a2: List[List[int]]) -> List[List[int]]:
        intersection = []
        i1 = 0
        i2 = 0
        while i1 < len(a1) and i2 < len(a2):
            if (a1[i1][0] >= a2[i2][0] and a1[i1][0] <= a2[i2][1]) or (a2[i2][0] >= a1[i1][0] and a2[i2][0] <= a1[i1][1]):
                intersection.append([ max(a1[i1][0], a2[i2][0]), min(a1[i1][1], a2[i2][1]) ])

            if a1[i1][1] < a2[i2][1]:
                i1 += 1
            else:
                i2 += 1

        return intersection
