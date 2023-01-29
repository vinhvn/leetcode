class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # convert number from 0-25 to corresponding alphabet char
        def getChar(num: int) -> str:
            return chr(ord('A') + num)

        res = []
        while columnNumber:
            curr = (columnNumber - 1) % 26
            res.insert(0, getChar(curr))
            columnNumber = (columnNumber - 1) // 26

        return "".join(res)
