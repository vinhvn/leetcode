class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        start = 0
        for end in range(len(arr)):
            if end >= m - 1:
                count = 1
                window = arr[start:end+1]
                i, j = start, end
                while count < k and j < len(arr):
                    i += m
                    j += m
                    if window == arr[i:j+1]:
                        count += 1
                    else:
                        break
                if count == k:
                    return True
                start += 1
        return False
