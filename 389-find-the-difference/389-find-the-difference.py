class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sCount = collections.Counter(s)
        tCount = collections.Counter(t)
        
        for c in t:
            if c not in sCount or sCount[c] != tCount[c]:
                return c

        return ""