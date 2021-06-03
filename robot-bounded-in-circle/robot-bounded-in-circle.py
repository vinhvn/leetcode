class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        coord = [0,0]
        di = 'n'
        
        for move in instructions:
            if di == 'n':
                if move == 'G':
                    coord[1] += 1
                elif move == 'L':
                    di = 'w'
                else:
                    di = 'e'
            elif di == 's':
                if move == 'G':
                    coord[1] -= 1
                elif move == 'L':
                    di = 'e'
                else:
                    di = 'w'
            elif di == 'e':
                if move == 'G':
                    coord[0] += 1
                elif move == 'L':
                    di = 'n'
                else:
                    di = 's'
            else:
                if move == 'G':
                    coord[0] -= 1
                elif move == 'L':
                    di = 's'
                else:
                    di = 'n'
        
        return coord == [0,0] or di != 'n'