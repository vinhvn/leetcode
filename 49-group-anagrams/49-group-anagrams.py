class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            charFreq = [0] * 26
            for char in s:
                charFreq[ord(char) - ord("a")] += 1
            key = ",".join([str(freq) for freq in charFreq])
            groups[key].append(s)

        return list(groups.values())
