class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n1n2 = nums[0]
        for i in range(1, len(nums)):
            n1n2 ^= nums[i]
        # find rightmost bit that is 1
        rightmost_set_bit = 1
        while rightmost_set_bit & n1n2 == 0:
            rightmost_set_bit = rightmost_set_bit << 1
        n1 = 0
        for num in nums:
            if num & rightmost_set_bit == 0:  # bit is not set
                n1 ^= num
        return [n1, n1n2 ^ n1]
