# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()

        def binary_search_peak(start: int, end: int) -> int:
            while start <= end:
                mid = start + (end - start) // 2
                # check if num is greater than its neighbors
                mid_num = mountain_arr.get(mid)
                midplus_num = mountain_arr.get(mid+1) if mid != n -1 else n-1
                midminus_num = mountain_arr.get(mid-1) if mid != 0 else 0
                if (
                    (mid == 0 and mid_num > midplus_num)
                    or (mid == n - 1 and midminus_num < mid_num)
                    or (midminus_num < mid_num and mid_num > midplus_num)
                ):
                    return mid
                # check if num is ascending or descending
                if mid != n - 1 and mid_num < midplus_num:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1

        def order_agnostic_binary_search(start: int, end: int, key: int, ascending: bool):
            while start <= end:
                mid = start + (end - start) // 2
                mid_num = mountain_arr.get(mid)
                if key == mid_num:
                    return mid
                if ascending:
                    if key < mid_num:
                        end = mid - 1 # key is in first half
                    else:
                        start = mid + 1 # key is in second half
                else:
                    if key > mid_num:
                        end = mid - 1 # key is in first half
                    else:
                        start = mid + 1 # key is in second half
            return -1 # not found

        peak = binary_search_peak(0, n-1)
        if peak == -1:
            return -1
        left = order_agnostic_binary_search(0, peak, target, True)
        right = order_agnostic_binary_search(peak, n-1, target, False)
        if left == -1 and right == -1:
            return -1
        elif left == -1:
            return right
        else:
            return left
