class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = len(nums)+1
        res = 0
        for i in range(num):
            res = res ^ i
        for i in nums:
            res = res ^ i
        return res