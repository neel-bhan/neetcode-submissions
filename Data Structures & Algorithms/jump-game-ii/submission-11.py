class Solution:
    def jump(self, nums: List[int]) -> int:
        reach = 0
        i = 0
        res = 0
        while reach < len(nums)-1:
            n = reach
            for j in range(i, n +1):
                reach = max(reach, j + nums[j])
            res += 1
        return res

