class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        def subset(i , s):
            if i >= len(nums):
                return
            s.append(nums[i])
            subset(i +1, s.copy())
            res.append(s.copy())
            s.pop()
            subset(i+1, s)
            

        subset(0, [])
        res.append([])
        return res