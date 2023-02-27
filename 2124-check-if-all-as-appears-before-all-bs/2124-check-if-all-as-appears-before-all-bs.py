class Solution:
    def checkString(self, s: str) -> bool:
        bSeen = False
        for i in range(len(s)):
            if s[i] == "a":
                if bSeen:
                    return False
            else:
                bSeen = True
        
        return True