class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        def binary_search():
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if x == nums[mid]:
                    return mid
                elif x < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            return end

        # get closest index to number matching x
        closest = binary_search()
        left, right = closest, closest + 1
        res = deque()
        for _ in range(k):
            # valid indices
            if left >= 0 and right < len(nums):
                diffLeft = abs(nums[left] - x)
                diffRight = abs(nums[right] - x)
                # compare diffs
                if diffLeft <= diffRight:
                    res.appendleft(nums[left])
                    left -= 1
                else:
                    res.append(nums[right])
                    right += 1
            elif left >= 0:  # right is beyond bounds
                res.appendleft(nums[left])
                left -= 1
            elif right < len(nums):  # left is beyond bounds
                res.append(nums[right])
                right += 1

        return list(res)
