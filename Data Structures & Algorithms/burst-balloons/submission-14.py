class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo =  {}

        nums.insert(0, 1)
        nums.append(1)

        def dfs(l, r):
            res = 0
            if (l, r) in memo:
                return memo[(l,r)]
            for i in range(l, r+1):
                res = max(res, (nums[i] * nums[l-1] * nums[r+1]) + dfs(l, i-1) + dfs(i+1, r))
            memo[(l,r)] = res
            return res
        res = dfs(1, len(nums)-2)

        return res
            
            
