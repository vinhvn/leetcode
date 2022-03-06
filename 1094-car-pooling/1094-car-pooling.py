class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # sort by start value
        trip_starts = sorted(trips, key=lambda x: x[1])
        trip_ends = sorted(trips, key=lambda x: x[2])
        cur_cap = i1 = i2 = 0
        while i1 < len(trips) and i2 < len(trips):
            if trip_starts[i1][1] < trip_ends[i2][2]:
                cur_cap += trip_starts[i1][0]
                i1 += 1
            else:
                cur_cap -= trip_ends[i2][0]
                i2 += 1
            
            if cur_cap > capacity:
                return False

        return cur_cap <= capacity
