class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        appeared = set()
        for num in nums:
            if num in appeared:
                return True
            appeared.add(num)
        return False