class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        use two pointers to iterate through sorted array
        if p2 finds a non-matching value, it's placed at p1 and p1 shifts one
        else p2 continues iterating
        """
        
        n = len(nums)
        p1 = 0
        p2 = 0
        
        while p2 < n:
            if nums[p2] != val:
                nums[p1] = nums[p2]
                p1 += 1
            
            p2 += 1
        
        return p1
    
        """
        Time complexity: O(n), linear time. The while loop will iterate over each element of nums once.
        Space compelxity: O(1), constant space. Two pointer variables are used to keep track of index positions.
        """