class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclidean_dist_origin(a: List[int]):
            return math.sqrt((a[0]) ** 2 + (a[1]) ** 2)

        maxHeap = []
        for coord in points:
            dist = euclidean_dist_origin(coord)
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (-dist, coord))
            elif dist < -maxHeap[0][0]:
                heapq.heappushpop(maxHeap, (-dist, coord))

        return [pair[1] for pair in maxHeap]