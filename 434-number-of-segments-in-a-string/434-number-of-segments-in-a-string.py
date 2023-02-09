class Solution:
    def countSegments(self, s: str) -> int:
        return len([segment for segment in s.split(" ") if segment])