class Solution:
    def isValid(self, s: str) -> bool:
        """
        hashmap of opening brackets and their corresponding closing bracket
        iterate through string
        push closing brackets to stack
        pop from stack and make sure closing brackets match
        """
        
        hashmap = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        
        valid = {
            "(", ")", "[", "]", "{", "}"
        }
        
        stack = []
        
        for c in s:
            if c in valid:
                if c in hashmap:
                    stack.append(hashmap[c])
                elif len(stack) == 0 or c != stack.pop():
                        return False
            else:
                return False
        
        return len(stack) == 0
        
        """
        n = len(s)
        Time complexity: O(n), linear time. The loop will iterate over each character in s once at most.
        Space complexity: O(n), linear space. The stack used will grow accordingly to keep track of the parentheses.
        """