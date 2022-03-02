import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build hashmap of num-frequency pairs
        num_freq = {}
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1
        # bucket sort, only works on basis that no frequency goes above n
        # make n buckets and add freq nums
        buckets = [[] for i in range(len(nums)+1)]
        for num, freq in num_freq.items():
            buckets[freq].append(num)
        output = []
        # iterate through highest frequencies
        for i in range(len(buckets)-1, -1, -1):
            if len(buckets[i]) > 0:
                for num in buckets[i]:
                    output.append(num)
                    if len(output) == k:
                        return output
        return output
