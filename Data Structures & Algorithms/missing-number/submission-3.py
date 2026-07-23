class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = len(nums)
        res = num
        for i in range(num):
            res ^= i ^ nums[i]
        return res