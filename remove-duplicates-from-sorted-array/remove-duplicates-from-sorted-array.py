class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        iterate through nums using two pointers
        set nums at p1 to p2 when p2 finds a different number
        """
        n = len(nums)
        if n < 2:
            return n
        
        prev = nums[0]
        p1 = 1
        p2 = 1
        while p2 < n:
            if nums[p2] != prev:
                nums[p1] = nums[p2]
                prev = nums[p2]
                p1 += 1
            
            p2 += 1
        
        return p1
        
        """
        Time complexity: O(n), linear time. The while loop iterates over each number in the array once.
        Space complexity: O(1), constant space. The only variables used are to track index positions and integer value.
        """