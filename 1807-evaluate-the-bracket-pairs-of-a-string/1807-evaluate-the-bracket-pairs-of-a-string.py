class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        # convert knowledge to hashmap
        knowledge_map = {}
        for key, value in knowledge:
            knowledge_map[key] = value
        
        # denote where opening and closing braces are
        start = end = 0
        output = ""
        for i in range(len(s)):
            if s[i] == "(":
                output += s[end:i]
                start = i+1
            elif s[i] == ")":
                end = i+1
                key = s[start:end-1]
                if key in knowledge_map:
                    output += knowledge_map[key]
                else:
                    output += "?"
        return output + s[end:i+1]
