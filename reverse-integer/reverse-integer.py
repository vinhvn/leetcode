class Solution:
    def reverse(self, x: int) -> int:
        # convert to abs
        # create a list of digits of x
        # reverse its digits
        # and convert list back into an int
        val = abs(x)
        lis = [i for i in str(val)]
        lis.reverse()
        n = int("".join(lis))
        if (x < 0):
            n *= -1
        
        # bounds checking
        if (n < -2**31 or n > (2**31) - 1):
            return 0
        
        return n