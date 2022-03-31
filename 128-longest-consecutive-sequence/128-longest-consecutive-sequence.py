class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0
        
        for num in hashset:
            if num-1 not in hashset:
                n = num
                streak = 1
                while n + 1 in hashset:
                    n += 1
                    streak += 1
                
                longest = max(longest, streak)
        
        return longest
