class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset = []
        res = []
        nums.sort()

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])

            dfs(i+1)
            subset.pop()
            while True:
                if i + 1 >= len(nums):
                    res.append(subset.copy())
                    return
                if nums[i+1] == nums[i]:
                    i += 1
                    continue
                break
            dfs(i+1)
        dfs(0)
        return res
