class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        n = len(nums)

        if target % 2 == 1:
            return False
        target//=2

        def dfs(i, sum):
            print(sum)
            if sum == target:
                return True
            if i >= n:
                return False
            return dfs(i+1, sum + nums[i]) or dfs(i+1, sum)
        return dfs(0, 0)
            

        
