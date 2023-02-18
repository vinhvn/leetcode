class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        greed = 0
        for size in s:
            if size >= g[greed]:
                greed += 1
                if greed == len(g):
                    break
        
        return greed
