class Solution:
    def jump(self, nums: List[int]) -> int:
        r = 0 
        res = 0

        for i in range(len(nums)):
            if r >= len(nums) -1:
                return res
            for j in range(i, r+1):
                r = max(r, j + nums[j])
            res += 1
        return -1
        