class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        #start dfs at each index
        #each index return max from starting there and taking it
        memo = {}
        def dfs(i, prev):
            if i >= len(nums):
                return 0
            if (i, prev) in memo:
                return memo[(i, prev)]
            res = dfs(i + 1, prev)
            if nums[i] > prev:
                res = max(res, 1+  dfs(i +1, nums[i]))
        
            memo[(i, prev)] = res
            return res
        return dfs(0, float('-inf'))



        