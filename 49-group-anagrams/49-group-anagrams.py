from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            sortedStr = str(sorted(s))
            if sortedStr not in groups:
                groups[sortedStr] = []
            groups[sortedStr].append(s)
        output = []
        for _, s in groups.items():
            output.append(s)
        return output
