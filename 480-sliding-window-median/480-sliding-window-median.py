import heapq

class Solution:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = [0.0 for _ in range(len(nums) - k + 1)]
        for i in range(len(nums)):
            self.add(nums[i])
            self.rebalance_heaps()
            if i >= k - 1:
                res[i - k + 1] = self.find_median()
                # find element to remove
                elem = nums[i - k + 1]
                if elem <= -self.maxHeap[0]:
                    self.remove(self.maxHeap, -elem)
                else:
                    self.remove(self.minHeap, elem)
                self.rebalance_heaps()

        return res

    def add(self, num):
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

    def rebalance_heaps(self):
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def find_median(self):
        if len(self.maxHeap) == len(self.minHeap):
            return -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0
        return -self.maxHeap[0] / 1.0

    def remove(self, heap, num):
        i = heap.index(num)
        heap[i] = heap[-1]
        del heap[-1]
        if i < len(heap):
            heapq._siftup(heap, i)
            heapq._siftdown(heap, 0, i)