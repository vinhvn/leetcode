class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        charCount = collections.Counter(words[0])
        for i in range(1, len(words)):
            wordCount = collections.Counter(words[i])
            keysToDelete = []
            for k, v in charCount.items():
                if k not in wordCount:
                    keysToDelete.append(k)
                    continue
                elif wordCount[k] != charCount[k]:
                    charCount[k] = min(charCount[k], wordCount[k])
            
            for k in keysToDelete:
                del charCount[k]

        res = []
        for k, v in charCount.items():
            for _ in range(v):
                res.append(k)
        
        return res