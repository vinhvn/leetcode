class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = {}
        max_len, max_freq, start = 0, 0, 0
        for end in range(len(s)):
            if s[end] not in char_freq:
                char_freq[s[end]] = 0
            char_freq[s[end]] += 1
            max_freq = max(max_freq, char_freq[s[end]])
            if end - start + 1 > max_freq + k:
                char_freq[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start + 1)
        return max_len