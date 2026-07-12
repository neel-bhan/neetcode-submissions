class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        li = [False] * len(nums)
        res = []
        subset = []
        def dfs():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            for i in range(len(nums)):
                if not li[i]:
                    subset.append(nums[i])
                    li[i] = True
                    dfs()
                    subset.pop()
                    li[i] = False
        dfs()
        return res
                    

           
        