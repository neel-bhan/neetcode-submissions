class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin = nums[0]
        curMax = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            temp = curMin
            curMin = min(curMax * nums[i], curMin * nums[i], nums[i])
            curMax = max(temp * nums[i], curMax * nums[i], nums[i])

            res = max(res, curMax, curMin)
        return res

