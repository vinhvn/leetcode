class Solution:
    def leastInterval(self, tasks: List[str], k: int) -> int:
        char_freq = defaultdict(int)
        for char in tasks:
            char_freq[char] += 1

        maxHeap = []
        for char, freq in char_freq.items():
            heapq.heappush(maxHeap, (-freq, char))

        intervals = 0
        while maxHeap:
            waitList = []
            n = k + 1  # try to execute up to k+1 tasks from the max heap
            while n > 0 and maxHeap:
                intervals += 1
                freq, char = heapq.heappop(maxHeap)
                if -freq > 1:
                    waitList.append((freq + 1, char))
                n -= 1

            # put all waitlisted tasks back onto the heap
            for freq, char in waitList:
                heapq.heappush(maxHeap, (freq, char))

            if maxHeap:
                intervals += n  # n idle intervals for the next iteration

        return intervals
