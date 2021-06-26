class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # dict to store complement (key) and index 
        d = {}
        
        for i in range(len(nums)):
            n = nums[i]
            # if number is in dict, we found a pair
            if n in d:
                return [d[n], i]
            else:
                d[target - n] = i
        
        # Time complexity: O(n)
        #   The algorithm will loop for n iterations at most once
        # Space complexity: O(n)
        #   This algorithm uses a hashmap which can grow up to n keys if no suitable complements can be found
