class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_freq = {}
        min_len, min_start, matches, start = len(s) + 1, 0, 0, 0
        for c in t:
            if c not in char_freq:
                char_freq[c] = 0
            char_freq[c] += 1
        for end in range(len(s)):
            end_char = s[end]
            if end_char in char_freq:
                char_freq[end_char] -= 1
                if char_freq[end_char] == 0:
                    matches += 1
            while matches == len(char_freq):
                if min_len > end - start + 1:
                    min_len = end - start + 1
                    min_start = start
                start_char = s[start]
                start += 1
                if start_char in char_freq:
                    if char_freq[start_char] == 0:
                        matches -= 1
                    char_freq[start_char] += 1
        if min_len == len(s) + 1:
            return ""
        return s[min_start : min_start + min_len]
