class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        pascals = [[] for j in range(numRows)]
        
        for i in range(numRows):
            for j in range(i + 1):
                if j == 0 or j == i:
                    pascals[i].append(1)
                else:
                    pascals[i].append(pascals[i - 1][j - 1] + pascals[i - 1][j])
        
        return pascals