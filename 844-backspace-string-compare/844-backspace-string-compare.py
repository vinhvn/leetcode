class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def getNextIndex(string: str, i: int):
            backspaces = 0
            while i >= 0:
                if string[i] == "#":
                    backspaces += 1
                elif backspaces > 0:
                    backspaces -= 1
                else:
                    break
                i -= 1
            return i
        
        p_s, p_t = len(s) - 1, len(t) - 1
        while p_s >= 0 or p_t >= 0:
            idx_s = getNextIndex(s, p_s)
            idx_t = getNextIndex(t, p_t)
            
            if idx_s < 0 and idx_t < 0:
                return True
            elif idx_s < 0 or idx_t < 0 or s[idx_s] != t[idx_t]:
                return False
            
            p_s = idx_s - 1
            p_t = idx_t - 1

        return True
