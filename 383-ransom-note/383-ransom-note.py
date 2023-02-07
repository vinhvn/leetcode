class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCount = collections.Counter(ransomNote)
        magazineCount = collections.Counter(magazine)
        
        for c in ransomCount:
            if c not in magazineCount or magazineCount[c] < ransomCount[c]:
                return False
        
        return True
    