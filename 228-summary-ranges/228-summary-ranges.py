class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]
        
        res = []
        start = nums[0]
        end = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                end = nums[i]
                continue
            
            res.append(str(start) if start == end else f"{start}->{end}")
            start = nums[i]
            end = nums[i]
        
        if not res or (start != res[-1][0]):
            res.append(str(start) if start == end else f"{start}->{end}")

        return res