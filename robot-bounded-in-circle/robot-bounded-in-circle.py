class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        compass = {
            'n': { 'L': 'w', 'R': 'e' },
            'e': { 'L': 'n', 'R': 's' },
            's': { 'L': 'e', 'R': 'w' },
            'w': { 'L': 's', 'R': 'n' }
        }
        changes = {
            'n': [0, 1],
            'e': [1, 0],
            's': [0, -1],
            'w': [-1, 0]
        }
        direction = 'n'
        coords = [0,0]
        for step in instructions:
            if step == 'G':
                x, y = changes[direction]
                coords[0] += x
                coords[0] += y
            else:
                direction = compass[direction][step]
        return coords == [0,0] or direction != 'n'