class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        for i in range(len(words)):
            lastChar = words[i][-1]
            firstChar = words[(i+1) % len(words)][0]
            if lastChar != firstChar:
                return False
        return True