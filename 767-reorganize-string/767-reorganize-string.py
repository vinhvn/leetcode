class Solution:
    def reorganizeString(self, s: str) -> str:
        # get char freqs
        char_freq = defaultdict(int)
        for char in s:
            char_freq[char] += 1
        # add all freq-char pairs to max heap
        maxHeap = []
        for char, freq in char_freq.items():
            heapq.heappush(maxHeap, (-freq, char))
        # build output list
        output = []
        prevChar, prevFreq = "", 0
        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            # add prev entry back into heap if it still has freq
            if prevChar and -prevFreq > 0:
                heapq.heappush(maxHeap, (prevFreq, prevChar))
            # append the current char to the output, decrement its freq
            output.append(char)
            prevChar = char
            prevFreq = freq + 1
        # return output list if all characters were appended
        return "".join(output) if len(output) == len(s) else ""
