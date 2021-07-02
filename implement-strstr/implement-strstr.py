class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        use python's built-in string.index()
        return if found, else return -1 for errors
        """

        out = 0

        try:
            out = haystack.index(needle)
        except ValueError:
            out = -1

        return out

        """
        Time complexity: O(n), linear time. At worst, must traverse entire string to look for needle.
        Space complexity: O(1), constant space. Only variable used is to track index.
        """