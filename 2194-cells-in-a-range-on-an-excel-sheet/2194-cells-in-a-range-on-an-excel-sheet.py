class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        rangeStart, rangeEnd = s.split(":")
        col1, row1 = ord(rangeStart[0]), int(rangeStart[1])
        col2, row2 = ord(rangeEnd[0]), int(rangeEnd[1])
        
        res = []
        for col in range(col1, col2 + 1):
            for row in range(row1, row2 + 1):
                res.append(chr(col) + str(row))
        
        return res
    