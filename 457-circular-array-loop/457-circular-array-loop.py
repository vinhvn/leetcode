class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def move(i, n, isForward):
            # not going same direction, return -1
            if (n >= 0) != isForward:
                return -1

            next = (i + n) % len(nums)
            if next < 0:
                next += len(nums)

            # one elem cycle
            if next == i:
                return -1
            return next

        # check every index for start of cycle
        for i in range(len(nums)):
            is_forward = nums[i] >= 0
            slow, fast = i, i

            while slow != -1 and fast != -1:
                slow = move(slow, nums[slow], is_forward)
                fast = move(fast, nums[fast], is_forward)
                if fast != -1:
                    fast = move(fast, nums[fast], is_forward)
                if slow != -1 and slow == fast:
                    return True
        return False
