class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # base case
        if len(s) != len(t):
            return False
        
        # populate hashmaps of char frequencies
        sFreq = defaultdict(int)
        tFreq = defaultdict(int)
        for i in range(len(s)):
            sFreq[s[i]] += 1
            tFreq[t[i]] += 1
        
        # compare hashmaps
        for char, freq in sFreq.items():
            if char not in tFreq or tFreq[char] != freq:
                return False
        
        return True
