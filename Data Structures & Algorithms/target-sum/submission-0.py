class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dfs(a, i):
            if i == len(nums):
                if a == target:
                    return 1
                else:
                    return 0
            res = dfs(a + nums[i], i +1) + dfs(a - nums[i], i + 1)
            return res
        return dfs(0,0)
            