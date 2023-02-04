class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        numsSet = set(nums)
        if len(numsSet) < 3:
            return max(numsSet)
        minHeap = []
        for n in numsSet:
            if len(minHeap) < 3:
                heapq.heappush(minHeap, n)
            elif minHeap[0] < n:
                heapq.heappushpop(minHeap, n)

        return minHeap[0]