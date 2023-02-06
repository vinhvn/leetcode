class Solution:
    def isSubsequence(self, pattern: str, string: str) -> bool:
        patternPtr = stringPtr = 0
        while patternPtr < len(pattern) and stringPtr < len(string):
            if pattern[patternPtr] == string[stringPtr]:
                patternPtr += 1
            stringPtr += 1
        if patternPtr >= len(pattern):
            return True
        return False