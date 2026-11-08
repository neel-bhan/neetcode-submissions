class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        half = s//2
        memo = {}
        def dfs(i, cur):
            if i >= len(nums):
                return False
            if cur == half:
                return True
            if (i, cur) in memo:
                return memo[(i, cur)]
            memo[(i, cur)] = dfs(i+1, cur + nums[i]) or dfs(i+1, cur)
            return memo[(i, cur)]
        return dfs(0,0)
