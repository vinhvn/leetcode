class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        evensCount = collections.Counter([n for n in nums if n % 2 == 0])
        res = -1
        maxFreq = 0
        for num, count in evensCount.items():
            if count > maxFreq:
                maxFreq = count
                res = num
            elif count == maxFreq:
                res = min(res, num)
        
        return res