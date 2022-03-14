class Solution:
    class ParenthesesString:
        def __init__(self, val="", numOpen=0, numClosed=0):
            self.val = val
            self.numOpen = numOpen
            self.numClosed = numClosed

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        queue = [Solution.ParenthesesString()]
        while queue:
            ps = queue.pop(0)
            # if max num of open and closed parentheses, add to res
            if ps.numOpen == n and ps.numClosed == n:
                res.append(ps.val)
                continue
            # if we can add an open parentheses, add it
            if ps.numOpen < n:
                queue.append(
                    Solution.ParenthesesString(
                        ps.val + "(", ps.numOpen + 1, ps.numClosed
                    )
                )
            # if we can add a closing parentheses, add it
            if ps.numOpen > ps.numClosed:
                queue.append(
                    Solution.ParenthesesString(
                        ps.val + ")", ps.numOpen, ps.numClosed + 1
                    )
                )
        return res
