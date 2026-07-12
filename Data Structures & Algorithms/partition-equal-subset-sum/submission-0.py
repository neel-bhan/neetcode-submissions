class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        def dfs(d, i):
            if i >= len(nums):
                return d == 0
            if (d, i) in memo:
                return memo[(d, i)]
            memo[(d,i)] = dfs(d + nums[i], i +1) or dfs(d - nums[i], i +1 )
            return memo[(d,i)]
        return dfs(0, 0)
            

        