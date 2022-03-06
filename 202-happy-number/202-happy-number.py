class Solution:
    def isHappy(self, num: int) -> bool:
        def square_sum(n: int):
            cur_sum = 0
            while n > 0:
                cur_sum += (n % 10) ** 2
                n = n // 10
            return cur_sum

        fast, slow = num, num
        while True:
            slow = square_sum(slow)
            fast = square_sum(square_sum(fast))
            if slow == fast:
                return slow == 1
