class Solution:
    def jump(self, nums: List[int]) -> int:

        l, r = 0, 0
        f = 0
        res = 0

        while r < len(nums) - 1:

            for i in range(l, r+1):
                f = max(f, nums[i] + i)
            l = r + 1
            r = f
            res += 1
        return res

        