class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        iterate over all strings in strs
        compare character at same index
        store end index of common string
        """
        
        end = -1
        for i in range(len(strs[0])):
            match = True
            c = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or c != s[i]:
                    match = False
                    break
            
            if match:
                end = i
            else:
                break
        
        return strs[0][:end+1] if end >= 0 else ""
        
        """
        n = num of chars in strs[0]
        m = num of strings in strs
        
        Time complexity: O(nm), linear time.
            The loop will iterate over the first n characters of each string
        Space complexity: O(1), constant space.
            The integer used to store the prefix end index stays constant.
        """
