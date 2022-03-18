class Solution:
    def flipAndInvertImage(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        for y in range(n):
            matrix[y].reverse()
            for x in range(n):
                matrix[y][x] ^= 1
        return matrix
