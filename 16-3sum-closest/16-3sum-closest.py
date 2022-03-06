class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_sum = min_diff = math.inf
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]
                cur_diff = abs(cur_sum - target)
                
                if cur_diff < min_diff:
                    min_diff = cur_diff
                    min_sum = cur_sum
                elif cur_diff == min_diff:
                    min_sum = min(min_sum, cur_sum)

                if cur_sum < target:
                    l += 1
                else:
                    r -= 1
        return min_sum
