class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # use a min heap to store min from each row
        minHeap = []
        for i in range(len(matrix)):
            # (value, index, row)
            heapq.heappush(minHeap, (matrix[i][0], 0, matrix[i]))

        # take smallest element from min heap until count is equal to k
        val = count = 0
        while minHeap:
            val, i, row = heapq.heappop(minHeap)
            count += 1
            if count == k:
                break
            # add next element from row
            if len(row) > i + 1:
                heapq.heappush(minHeap, (row[i + 1], i + 1, row))

        return val
