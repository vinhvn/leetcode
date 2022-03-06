class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        quadruplets = []
        for i in range(n-3):
            if i > 0 and nums[i-1] == nums[i]:
                continue

            for j in range(i+1, n-2):
                if j > i+1 and nums[j-1] == nums[j]:
                    continue
                l, r = j+1, n-1
                
                while l < r:
                    cur_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    
                    if cur_sum == target:
                        quadruplets.append([ nums[i], nums[j], nums[l], nums[r] ])
                        l += 1
                        while l < r and nums[l-1] == nums[l]:
                            l += 1
                    elif cur_sum < target:
                        l += 1
                    else:
                        r -= 1
        return quadruplets
