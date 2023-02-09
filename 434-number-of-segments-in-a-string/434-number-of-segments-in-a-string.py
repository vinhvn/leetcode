class Solution:
    def countSegments(self, s: str) -> int:
        words = s.split(" ")
        return len([word for word in words if word])