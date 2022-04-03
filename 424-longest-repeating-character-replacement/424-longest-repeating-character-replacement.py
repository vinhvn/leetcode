class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charFreq = defaultdict(int)
        maxLen, majority, start = 0, 0, 0
        for end in range(len(s)):
            charFreq[s[end]] += 1
            majority = max(majority, charFreq[s[end]])
            if end - start + 1 > majority + k:
                charFreq[s[start]] -= 1
                start += 1
            maxLen = max(maxLen, end - start + 1)
        return maxLen
