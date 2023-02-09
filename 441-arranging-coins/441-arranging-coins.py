class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = 2
        while n > 0:
            n -= k
            k += 1
        return k - 2

# [0] => 0
# [1,2] => 1
# [3,4,5] => 2
# [6,7,8,9] => 3
# [10,11,12,13,14] => 4
# [15,16,17,18,19,20] => 5