class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        n = len(nums)
        memo = {}
        if target % 2 == 1:
            return False
        target//=2

        def dfs(i, sum):

            if sum == target:
                return True
            if i >= n or sum > target:
                return False
            if (i, sum) in memo:
                return memo[(i, sum)]
            memo[(i, sum)]=  dfs(i+1, sum + nums[i]) or dfs(i+1, sum)
            return memo[(i, sum)]
        return dfs(0, 0)
            

        
