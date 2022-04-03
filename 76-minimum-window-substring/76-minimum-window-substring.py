class Solution:
    def minWindow(self, s: str, t: str) -> str:
        patternFreq = defaultdict(int)
        for char in t:
            patternFreq[char] += 1
        matches = 0
        minStart, minEnd = 0, math.inf
        # sliding window
        start = 0
        for end in range(len(s)):
            if s[end] in patternFreq:
                patternFreq[s[end]] -= 1
                if patternFreq[s[end]] == 0:
                    matches += 1
            
            while start <= end and matches == len(patternFreq):
                # update min
                if minEnd - minStart > end - start:
                    minStart, minEnd = start, end
                if s[start] in patternFreq:
                    if patternFreq[s[start]] == 0:
                        matches -= 1
                    patternFreq[s[start]] += 1
                start += 1
        
        if minEnd == math.inf:
            return ""
        return s[minStart : minEnd+1]
