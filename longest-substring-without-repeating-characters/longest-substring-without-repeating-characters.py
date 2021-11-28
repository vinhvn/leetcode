class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        start = 0
        chars = {}
        for end in range(len(s)):
            if s[end] not in chars:
                chars[s[end]] = 1
                longest = max(longest, end-start+1)
            else:
                chars[s[end]] += 1
            
            while (len(chars) < end-start+1):
                chars[s[start]] -= 1
                if chars[s[start]] == 0:
                    del chars[s[start]]
                start += 1
        return longest
            