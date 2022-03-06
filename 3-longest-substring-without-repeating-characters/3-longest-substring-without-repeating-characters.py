class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        max_len, start = 0, 0
        for end in range(len(s)):
            if s[end] in char_index:
                start = max(start, char_index[s[end]] + 1)
            char_index[s[end]] = end
            max_len = max(max_len, end - start + 1)
        return max_len
