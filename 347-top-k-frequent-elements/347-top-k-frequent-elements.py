import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build hashmap of num-frequency pairs
        num_freq = {}
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) - 1
        # add all to heap
        heap = []
        for key, val in num_freq.items():
            heapq.heappush(heap, (val, key))
        output = []
        # pop max k
        for i in range(k):
            output.append(heapq.heappop(heap)[1])
        return output
