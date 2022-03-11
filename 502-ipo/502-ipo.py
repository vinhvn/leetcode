class Solution:
    def findMaximizedCapital(self, numProjects: int, initialCapital: int, profits: List[int], capitals: List[int]) -> int:
        minCapitalHeap = []
        maxProfitHeap = []
        # insert all capitals into min heap
        for i in range(len(capitals)):
            heapq.heappush(minCapitalHeap, (capitals[i], i))
        # try to find 'numProjects' best projects
        availableCapital = initialCapital
        for _ in range(numProjects):
            # find all projects that can be purchased with
            # available capital and place them into a max heap
            while minCapitalHeap and minCapitalHeap[0][0] <= availableCapital:
                capital, i = heapq.heappop(minCapitalHeap)
                heapq.heappush(maxProfitHeap, (-profits[i], i))
            # terminate if none are found
            if not maxProfitHeap:
                break
            # select project with max profit
            availableCapital += -heapq.heappop(maxProfitHeap)[0]

        return availableCapital
