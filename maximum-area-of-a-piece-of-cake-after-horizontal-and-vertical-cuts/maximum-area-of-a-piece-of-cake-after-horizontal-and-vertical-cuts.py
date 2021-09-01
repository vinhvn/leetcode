class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        max_width = 0
        max_height = 0
        horizontalCuts.sort()
        for i in range(len(horizontalCuts) + 1):
            if i == 0:
                diff = horizontalCuts[i]
            elif i == len(horizontalCuts):
                diff = h - horizontalCuts[i-1]
            else:
                diff = horizontalCuts[i] - horizontalCuts[i-1]
            max_height = max(max_height, diff)
        verticalCuts.sort()
        for i in range(len(verticalCuts) + 1):
            if i == 0:
                diff = verticalCuts[i]
            elif i == len(verticalCuts):
                diff = w - verticalCuts[i-1]
            else:
                diff = verticalCuts[i] - verticalCuts[i-1]
            max_width = max(max_width, diff)
        return (max_width * max_height) % (10**9 + 7)