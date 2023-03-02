class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        numCount = collections.Counter(nums)
        minHeap = []
        
        for k, v in numCount.items():
            heapq.heappush(minHeap, (v, -k))
        
        res = []
        while minHeap:
            v, k = heapq.heappop(minHeap)
            res = res + [-k] * v
        
        return res
    