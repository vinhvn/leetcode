class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        targetCount = defaultdict(int)
        maxTarget, maxCount = -1, -1
        for i in range(1, len(nums)):
            if nums[i-1] == key:
                target = nums[i]
                targetCount[target] += 1
                if targetCount[target] > maxCount:
                    maxCount = targetCount[target]
                    maxTarget = target
        
        return maxTarget
            