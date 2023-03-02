class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        minHeap = []
        for i in range(n):
            heapq.heappush(minHeap, (-heights[i], names[i]))
        
        res = []
        while minHeap:
            res.append(heapq.heappop(minHeap)[1])
        
        return res
    