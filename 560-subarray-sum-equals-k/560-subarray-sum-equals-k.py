class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        hashmap[0] = 1
        output = 0
        curSum = 0
        for num in nums:
            curSum += num
            if curSum - k in hashmap:
                output += hashmap[curSum - k]
            hashmap[curSum] += 1
        return output
