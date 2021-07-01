class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        create a set containing all elements of nums
        compare the length of the set against the length of the list
        if equal, the list contains no duplicates
        """
        return len(set(nums)) != len(nums)
        
        """
        n = len(nums)
        Time complexity: O(n), linear time. Creating a set of all elements of nums will iterate over each element of nums at least once.
        Space complexity: O(n), linear space. The set will contain all elements of nums at most.
        """