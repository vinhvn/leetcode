class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        validChars = list(s)
        for i, char in enumerate(validChars):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    validChars[i] = ""
        
        for index in stack:
            validChars[index] = ""

        return "".join(validChars)
