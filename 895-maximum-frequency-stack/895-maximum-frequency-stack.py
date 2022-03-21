class FreqStack:

    def __init__(self):
        self.maxHeap = []
        self.freqMap = defaultdict(int)
        self.i = 0

    def push(self, num: int) -> None:
        self.freqMap[num] += 1
        heapq.heappush(self.maxHeap, (-self.freqMap[num], -self.i, num))
        self.i += 1

    def pop(self) -> int:
        _, _, num = heapq.heappop(self.maxHeap)
        # decrement freq or remove if last
        if self.freqMap[num] > 1:
            self.freqMap[num] -= 1
        else:
            del self.freqMap[num]
        return num


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()