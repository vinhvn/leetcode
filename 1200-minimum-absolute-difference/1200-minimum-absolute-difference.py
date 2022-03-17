class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = math.inf
        output = [[]]
        for i in range(1, len(arr)):
            diff = abs(arr[i-1] - arr[i])
            if diff < minDiff:
                minDiff = diff
                output = [[arr[i-1], arr[i]]]
            elif diff == minDiff:
                output.append([arr[i-1], arr[i]])
        return output
