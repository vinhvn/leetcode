class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboardRowSets = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm")
        ]
        
        res = []
        for word in words:
            for rowSet in keyboardRowSets:
                wordSet = set(word.lower())
                if wordSet.issubset(rowSet):
                    res.append(word)
                    break
        
        return res