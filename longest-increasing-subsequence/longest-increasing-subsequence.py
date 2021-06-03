class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        data = [1 for i in range(n)]
        
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i, -1):
                if (nums[i] < nums[j]):
                    data[i] = max(data[i], data[j] + 1)
        print(data)
        return max(data)