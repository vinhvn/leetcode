class Solution:
    def nextGreatestLetter(self, chars: List[str], key: str) -> str:
        start, end = 0, len(chars) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if key < chars[mid]:
                end = mid - 1
            else:
                start = mid + 1
        # circular array modification
        if start >= len(chars):
            start = 0
        return chars[start]
