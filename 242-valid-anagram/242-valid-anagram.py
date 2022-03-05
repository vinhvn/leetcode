class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_freq = {}
        for char in s:
            s_freq[char] = s_freq.get(char, 0) + 1
        t_freq = {}
        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1
        for key in s_freq:
            if key not in t_freq or s_freq[key] != t_freq[key]:
                return False
        return True
