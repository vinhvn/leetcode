class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numFreq = defaultdict(int)
        goodPairs = 0
        for num in nums:
            numFreq[num] += 1
            if numFreq[num] > 1:
                goodPairs += numFreq[num] - 1
        return goodPairs
