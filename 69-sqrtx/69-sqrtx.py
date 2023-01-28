class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        l, r = 0, x
        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            square = mid * mid
            if square <= x:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res
