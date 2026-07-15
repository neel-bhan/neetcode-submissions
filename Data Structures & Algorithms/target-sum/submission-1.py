class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(a, i):
            if i == len(nums):
                if a == target:
                    return 1
                else:
                    return 0
            if (a, i) in memo:
                return memo[(a, i)]
            memo[(a, i)] = dfs(a + nums[i], i +1) + dfs(a - nums[i], i + 1)
            return memo[(a, i)]
        return dfs(0,0)
            