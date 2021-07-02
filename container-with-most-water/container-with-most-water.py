class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        brute-force solution
        use two pointers to iterate
        available height = min(height1, height2)
        calculate area and return max area found
        """
        
        maxArea = 0
        p1 = 0
        p2 = len(height) - 1
        
        while p1 < p2:
            h = min(height[p1], height[p2])
            b = p2 - p1
            area = h * b
            maxArea = max(maxArea, area)
            
            if h == height[p2]:
                p2 -= 1
            else:
                p1 += 1
        
        return maxArea