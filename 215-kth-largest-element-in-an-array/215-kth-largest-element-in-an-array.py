import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []  # only grows up to k in size
        for num in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, num)
            elif num > minHeap[0]:
                heapq.heapreplace(minHeap, num)
        # at this point, minHeap[0] will be the minimum out of the k greatest
        return minHeap[0]
