class Solution:
    def checkInclusion(self, p: str, s: str) -> bool:
        char_freq = {}
        matches, start = 0, 0
        for c in p:
            if c not in char_freq:
                char_freq[c] = 0
            char_freq[c] += 1
        for end, end_char in enumerate(s):
            if end_char in char_freq:
                char_freq[end_char] -= 1
                if char_freq[end_char] == 0:
                    matches += 1
            if matches == len(char_freq):
                return True
            if end >= len(p) - 1:
                start_char = s[start]
                start += 1
                if start_char in char_freq:
                    if char_freq[start_char] == 0:
                        matches -= 1
                    char_freq[start_char] += 1
        return False
