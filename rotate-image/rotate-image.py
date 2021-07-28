class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for y in range(0, n//2):
            for x in range(y, n-y-1):
                temp = matrix[y][x]
                matrix[y][x] = matrix[n-x-1][y]
                matrix[n-x-1][y] = matrix[n-y-1][n-x-1]
                matrix[n-y-1][n-x-1] = matrix[x][n-y-1]
                matrix[x][n-y-1] = temp