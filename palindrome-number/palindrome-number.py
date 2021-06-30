class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        convert integer x to a string
        create a reversed string
        compare them for equality
        """
        
        lis = str(x)
        rev = lis[::-1]
        return lis == rev
        