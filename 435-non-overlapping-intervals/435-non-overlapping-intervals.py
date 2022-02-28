class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by starting times
        intervals.sort(key=lambda x: x[0])
        # greedy, make decision at each iteration
        removals = 0
        
        i = 1
        while i < len(intervals):
            # check for overlap
            if intervals[i-1][1] > intervals[i][0]:
                # remove interval with later end
                removals += 1
                if intervals[i-1][1] > intervals[i][1]:
                    intervals.pop(i-1)
                else:
                    intervals.pop(i)
            else:
                i += 1

        return removals
    