class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currStreak = nums[0]
        maxStreak = currStreak
        for i in range(1, len(nums)):
            if nums[i] == 1:
                if nums[i-1] == 0:
                    currStreak = 1
                else:
                    currStreak += 1
                maxStreak = max(maxStreak, currStreak)
            else:
                currStreak = 0
        return maxStreak