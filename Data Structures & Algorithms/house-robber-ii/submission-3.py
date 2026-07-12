class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [[-1] * 2 for _ in range(len(nums))]

        def dfs(i, inc):
            if i == len(nums) -1:
                if inc:
                    return 0
                else:
                    return nums[i]
            
            if i >= len(nums):
                return 0    
            if memo[i][inc] != -1:
                return memo[i][inc]
            
            if i == 0:
                ans = max(nums[0] + dfs(i+2, True), dfs(i+1, False))
            else:
                ans = max(nums[i] + dfs(i+2, inc), dfs(i+1, inc))
            memo[i][inc] = ans
            return memo[i][inc]
        return dfs(0, False)

        