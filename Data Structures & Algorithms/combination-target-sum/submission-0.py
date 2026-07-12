class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sum = 0
        subset = []
        res = []
        def dfs(i, sum ):
            if sum > target or i >= len(nums):
                return
            if sum == target:
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i, sum + nums[i])
            subset.pop()
            dfs(i+1, sum)
        dfs(0,0)
        return res


            