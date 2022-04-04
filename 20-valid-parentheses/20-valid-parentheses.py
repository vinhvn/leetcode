class Solution:
    def isValid(self, s: str) -> bool:
        opening = set("({[")
        closingMap = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        stack = []
        
        for char in s:
            if char not in opening and char not in closingMap:
                return False
            
            if char in opening:
                stack.append(char)
            elif len(stack) == 0 or closingMap[char] != stack.pop():
                return False

        return len(stack) == 0
