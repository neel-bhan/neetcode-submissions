class Solution:
    def jump(self, nums: List[int]) -> int:
        r = 0 
        res = 0
        i = 0
        while r < len(nums) -1:
            farthest = 0
            for j in range(i, r+1):
                farthest = max(farthest, j + nums[j])
            i = r + 1
            r = farthest
            res += 1
        return res
        