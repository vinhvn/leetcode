class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = []
        currSum = 0
        for n in nums:
            currSum += n
            self.sums.append(currSum)

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right] - (self.sums[left - 1] if left > 0 else 0)


# nums = [-2,0,3,-5,2,-1]
# leftSums = [-2,-2,1,-4,-2,-3]
# rightSums = [-3,-1,-1,-4,1,-1]
# [0,2],[2,5],[0,5]
# [null,1,-1,-3]

# sumRange(0,2) -> leftSums[2] -> 1
# sumRange(2,5) -> leftSums[5] - leftSums[1] -> -1
# sumRange(0,5) -> leftSums[5] -> -3
# sumRange(1,4) -> leftSums[4] - leftSums[0] -> 0
