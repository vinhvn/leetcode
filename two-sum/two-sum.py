class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        # dict to store complement (key) and index 
        hashmap = {}
        
        for i in range(len(nums)):
            val = nums[i]
            # if number is in dict, we found a pair
            # else, we put in the complement we want to find
            if val in hashmap:
                return [hashmap[val], i]
            else:
                hashmap[target - val] = i
        
        """
        n = len(nums)
        Time complexity: O(n), linear time. Loops over each element of nums once at most.
        
        Space complexity: O(n), linear space. The hashmap grows up to n keys if no suitable complements can be found
        """
