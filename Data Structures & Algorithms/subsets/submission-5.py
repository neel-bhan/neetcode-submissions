class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        def subset(i ):
            if i >= len(nums):
                res.append(cur.copy())
                return
            cur.append(nums[i])
            subset(i +1)
            cur.pop()
            subset(i+1)
            

        subset(0)
        return res