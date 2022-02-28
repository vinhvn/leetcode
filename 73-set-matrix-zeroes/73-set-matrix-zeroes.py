class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        firstRowZero = False
        firstColZero = False
        # check if first col has zero
        for y in range(m):
            if matrix[y][0] == 0:
                firstColZero = True
                break
        # check if first row has zero
        for x in range(n):
            if matrix[0][x] == 0:
                firstRowZero = True
                break
        
        # use first row/col to store rows/cols to zero later on
        for y in range(1, m):
            for x in range(1, n):
                if matrix[y][x] == 0:
                    matrix[y][0] = 0
                    matrix[0][x] = 0
        
        # zero rows
        for y in range(1, m):
            if matrix[y][0] == 0:
                for x in range(1, n):
                    matrix[y][x] = 0
        # zero cols
        for x in range(1, n):
            if matrix[0][x] == 0:
                for y in range(1, m):
                    matrix[y][x] = 0
        
        # zero first row and col if needed
        if firstRowZero:
            for x in range(n):
                matrix[0][x] = 0
        if firstColZero:
            for y in range(m):
                matrix[y][0] = 0
        