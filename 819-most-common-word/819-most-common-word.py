class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        formatted = re.sub(r'[^\w\s]', ' ', paragraph).lower()
        wordCount = collections.Counter([word for word in formatted.split(" ") if word])
        bannedSet = set(banned)
        
        maxWord, maxFreq = "", 0
        for word, freq in wordCount.items():
            if word not in bannedSet and freq > maxFreq:
                maxWord = word
                maxFreq = freq
        return maxWord