class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        maxStartHeap = []
        maxEndHeap = []
        res = [-1] * len(intervals)
        # populate all heaps
        for i in range(len(intervals)):
            heapq.heappush(maxStartHeap, (-intervals[i][0], i))
            heapq.heappush(maxEndHeap, (-intervals[i][1], i))
        # calculate all next intervals
        for _ in range(len(res)):
            topEnd, endIdx = heapq.heappop(maxEndHeap)
            # check if max start comes after current max end
            if -maxStartHeap[0][0] >= -topEnd:
                topStart, startIdx = heapq.heappop(maxStartHeap)
                # find interval with closest start
                while maxStartHeap and -maxStartHeap[0][0] >= -topEnd:
                    topStart, startIdx = heapq.heappop(maxStartHeap)
                res[endIdx] = startIdx
                # put interval back in for next iterations
                heapq.heappush(maxStartHeap, (topStart, startIdx))

        return res
