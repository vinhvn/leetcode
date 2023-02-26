class Solution:
    def averageValue(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for n in nums:
            # even and divisible by 3
            if n % 2 == 0 and n % 3 == 0:
                res += n
                count += 1
        
        return res // count if count > 0 else res