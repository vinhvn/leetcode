class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        squares = [0 for i in range(len(nums))]
        next_square = len(squares) - 1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                squares[next_square] = nums[l] ** 2
                l += 1
            else:
                squares[next_square] = nums[r] ** 2
                r -= 1
            next_square -= 1
        return squares
