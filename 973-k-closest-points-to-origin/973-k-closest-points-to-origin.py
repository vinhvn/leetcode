class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for coord in points:
            dist = coord[0] ** 2 + coord[1] ** 2
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (-dist, coord))
            elif dist < -maxHeap[0][0]:
                heapq.heappushpop(maxHeap, (-dist, coord))

        return [pair[1] for pair in maxHeap]
