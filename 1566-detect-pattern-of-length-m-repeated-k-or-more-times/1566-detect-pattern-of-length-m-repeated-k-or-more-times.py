class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        count = 0
        for i in range(len(arr) - m):
            if (arr[i] != arr[i+m]):
                count = 0
                continue
            count += 1
            if count == (k-1)*m:
                return True
        return False
