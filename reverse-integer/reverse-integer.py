class Solution:
    def reverse(self, x: int) -> int:
        """
        convert to absolute value and stringify value
        reverse its digits and convert back into an int
        """
    
        n = int(str(abs(x))[::-1])
        if (x < 0):
            n *= -1
        
        if (n < -2**31 or n > (2**31) - 1):
            return 0
        
        return n
    
        """
        n = number of digits in x
        Time complexity: O(n). We must traverse over each digit in order to stringify and reverse it.
        Space complexity: O(n). We store the string version of integer x in order to reverse it.
        """