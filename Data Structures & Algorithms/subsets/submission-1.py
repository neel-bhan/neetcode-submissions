class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        li = []
        
        def dfs(i):
            if i >= len(nums):
                return
        
            li.append(nums[i])
            dfs(i+1)
            res.append(li.copy())
            li.pop()
            dfs(i+1)
        dfs(0)
        return res
            
            
            