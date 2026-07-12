class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        li = []
        
        def dfs(i):
            if i >= len(nums):
                res.append(li.copy())
                return
        
            li.append(nums[i])
            dfs(i+1)
            li.pop()
            dfs(i+1)
        dfs(0)
        return res
            
            
            