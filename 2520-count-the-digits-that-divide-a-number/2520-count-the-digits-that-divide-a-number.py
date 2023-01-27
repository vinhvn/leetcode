class Solution:
    def countDigits(self, num: int) -> int:
        divisors = 0
        n = num
        while n:
            digit = n % 10
            if num % digit == 0:
                divisors += 1
            n //= 10
        return divisors