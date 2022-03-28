class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        # if sum is odd, 2 equal sums cannot add up to it
        if s % 2 == 1:
            return False
        
        target = s // 2
        dp = [[False for _ in range(target+1)] for _ in range(len(nums))]
        
        # populate sum=0 column
        for j in range(len(nums)):
            dp[j][0] = True
        
        # with only 1 number, its only true if the sum is equal to the number
        for i in range(1, target+1):
            dp[0][i] = nums[0] == i
        
        # process rest of subsets
        for i in range(1, len(nums)):
            for j in range(1, target+1):
                # if we can get target without including current number
                if dp[i-1][j]:
                    dp[i][j] = dp[i-1][j]
                elif j >= nums[i]: # if there is space for num at i to reach target
                    dp[i][j] = dp[i-1][j - nums[i]]
        
        return dp[len(nums)-1][target]
