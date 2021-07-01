class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        iterate over all strings in strs
        compare character at same index
        store common characters
        """
        
        prefix = ""
        for i in range(len(strs[0])):
            match = True
            c = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or c != s[i]:
                    match = False
                    break
            
            if match:
                prefix += c
            else:
                return prefix
        
        return prefix
            