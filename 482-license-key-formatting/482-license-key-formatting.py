class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper()
        res = deque()
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != "-":
                res.appendleft(s[i])
                count += 1
                if count >= k:
                    res.appendleft("-")
                    count = 0

        if res and res[0] == "-":
            res.popleft()
        return "".join(res)