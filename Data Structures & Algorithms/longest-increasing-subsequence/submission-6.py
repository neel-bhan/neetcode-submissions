class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i, cur):
            if i >= len(nums):
                return 0
            if (i, cur) in memo:
                return memo[(i,cur)]
            num = 0
            if nums[i] > cur:
                num = 1 + dfs(i+1, nums[i])
            num = max(num, dfs(i+1, cur))
            memo[(i, cur)] = num
            return num

        return dfs(0, -1001)
        