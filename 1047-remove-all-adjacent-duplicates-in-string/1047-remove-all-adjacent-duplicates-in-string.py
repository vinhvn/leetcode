class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = list(s)
        i = 1
        while i < len(res):
            if res[i-1] == res[i]:
                res.pop(i)
                res.pop(i-1)
                i = max(1, i-1)
            else:
                i += 1

        return "".join(res)
        