class Solution:
    def climbStairs(self, n: int) -> int:
        def fib(num):
            entries = [0] * (n+1)
            entries[0] = 1
            entries[1] = 1
            for i in range(2, num+1):
                entries[i] += entries[i-1] + entries[i-2] 
            return entries[num]
        return fib(n)