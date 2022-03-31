class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # cant make triplets with less than 3 elements
        if len(nums) < 3:
            return []
        
        # sort input array in ascending order
        nums.sort()
        triplets = []
        for i in range(len(nums)-2):
            # avoid duplicates
            if i > 0 and nums[i-1] == nums[i]:
                continue

            # use a two pointer approach
            l = i + 1
            r = len(nums) - 1
            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                
                # if we find a zero triplet, add it to output
                if summ == 0:
                    triplets.append([ nums[i], nums[l], nums[r] ])
                    l += 1
                    # make sure we don't add another duplicate
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                elif summ < 0: # if our sum is too small, increment left pointer
                    l += 1
                else: # otherwise, we decrement right pointer
                    r -= 1
        
        return triplets
