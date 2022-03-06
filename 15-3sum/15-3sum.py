class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        
        nums.sort()
        triplets = []
        target = 0
        for i in range(n - 2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l, r = i+1, n-1
            
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == target:
                    triplets.append([ nums[i], nums[l], nums[r] ])
                    l += 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                elif sum < target:
                    l += 1
                else:
                    r -= 1
        return triplets
