class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i, first):
            if i >= len(nums):
                return 0
            if (i, first) in memo:
                return memo[(i, first)]
            if i == 0:
                memo[(i, first)] = max(nums[i] + dfs(i+2, True), dfs(i+1, False))
            elif i == len(nums)-1 and first:
                return 0
            else:
                memo[(i, first)] = max(nums[i] + dfs(i+2, first), dfs(i+1, first))
            return memo[(i, first)]
        return dfs(0, False)



        

        