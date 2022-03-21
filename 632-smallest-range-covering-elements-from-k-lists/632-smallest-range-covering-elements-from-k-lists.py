class Solution:
    def smallestRange(self, lists: List[List[int]]) -> List[int]:
        minHeap = []
        # add all first elements to heap, track max
        currMax = -math.inf
        for lis in lists:
            heapq.heappush(minHeap, (lis[0], 0, lis))
            currMax = max(currMax, lis[0])

        # take smallest from min heap, update range if it gives smaller range
        start, end = 0, math.inf
        # break if one list is no longer included in the heap
        while len(minHeap) == len(lists):
            num, i, lis = heapq.heappop(minHeap)
            if end - start > currMax - num:
                start = num
                end = currMax
            # add next element if it exists
            if i < len(lis) - 1:
                heapq.heappush(minHeap, (lis[i + 1], i + 1, lis))
                currMax = max(currMax, lis[i + 1])

        return [start, end]
