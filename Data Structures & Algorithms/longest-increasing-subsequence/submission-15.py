class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        #start dfs at each index
        #each index return max from starting there and taking it
        memo = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            res = 1
            if i in memo:
                return memo[i]
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    res = max(res, 1 + dfs(j))
            memo[i] = res
            return res
        return max(dfs(i) for i in range(len(nums)))



        