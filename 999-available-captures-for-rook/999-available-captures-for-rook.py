class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def getRookPosition(board: List[List[str]]) -> Tuple[int, int]:
            for y in range(len(board)):
                for x in range(len(board[y])):
                    if board[y][x] == "R":
                        return (x, y)
            
            return (-1, -1)
        
        def checkCapture(board: List[List[str]], x: int, y: int) -> int:
            if board[y][x] == "B":
                return -1
            elif board[y][x] == "p":
                return 1
            else:
                return 0
        
        def getCaptures(board: List[List[str]], rookPos: Tuple[int, int]) -> int:
            captures = 0

            # check file above
            for y in range(rookPos[1] - 1, -1, -1):
                code = checkCapture(board, rookPos[0], y)
                if code == -1:
                    break
                elif code == 1:
                    captures += 1
                    break

            # check file below
            for y in range(rookPos[1] + 1, len(board)):
                code = checkCapture(board, rookPos[0], y)
                if code == -1:
                    break
                elif code == 1:
                    captures += 1
                    break
            
            # check rank left
            for x in range(rookPos[0] - 1, -1, -1):
                code = checkCapture(board, x, rookPos[1])
                if code == -1:
                    break
                elif code == 1:
                    captures += 1
                    break
            
            # check rank right
            for x in range(rookPos[0] + 1, len(board[0])):
                code = checkCapture(board, x, rookPos[1])
                if code == -1:
                    break
                elif code == 1:
                    captures += 1
                    break
            
            return captures
        
        rookPos = getRookPosition(board)
        res = getCaptures(board, rookPos)
        
        return res