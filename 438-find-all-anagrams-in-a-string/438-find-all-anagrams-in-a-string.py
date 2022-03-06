class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        char_freq = {}
        indices = []
        matches, start = 0, 0
        for char in p:
            if char not in char_freq:
                char_freq[char] = 0
            char_freq[char] += 1
        for end in range(len(s)):
            end_char = s[end]
            if end_char in char_freq:
                char_freq[end_char] -= 1
                if char_freq[end_char] == 0:
                    matches += 1
            if matches == len(char_freq):
                indices.append(start)
            if end >= len(p) - 1:
                start_char = s[start]
                start += 1
                if start_char in char_freq:
                    if char_freq[start_char] == 0:
                        matches -= 1
                    char_freq[start_char] += 1
        return indices
