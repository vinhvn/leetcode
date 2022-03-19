class Solution:
    def frequencySort(self, string: str) -> str:
        char_freq = defaultdict(int)
        for char in string:
            char_freq[char] += 1
        maxHeap = []
        for char in char_freq:
            heapq.heappush(maxHeap, (-char_freq[char], char))
        output = []
        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            output.append(-freq * char)
        return "".join(output)
