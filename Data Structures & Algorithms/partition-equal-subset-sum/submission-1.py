class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        total = sum(nums) // 2 
        total = sum(nums)

        if total % 2 == 1:

            return False

        total = total // 2
        def dfs(d, i):
            if d == total:
                return True
            if i >= len(nums) or d > total:
                return False
            if (d, i) in memo:
                return memo[(d, i)]
            memo[(d,i)] = dfs(d + nums[i], i +1) or dfs(d, i +1 )
            return memo[(d,i)]
        return dfs(0, 0)
            

        