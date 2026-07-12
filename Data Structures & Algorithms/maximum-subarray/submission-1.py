class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        res = 0 
        p = 0
        res = nums[0]
        while p < len(nums):
            cur += nums[p]
            res = max(nums[p], res)
            p+=1
            if cur <= 0:
                cur = 0
            else:
                res = max(res, cur)

        return res
