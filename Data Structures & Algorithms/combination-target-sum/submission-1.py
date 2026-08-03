class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        def subset(i, sum):
            if sum > target:
                return
            if i >= len(nums):
                if sum == target:
                    res.append(cur.copy())
                return
            cur.append(nums[i])
            subset(i, sum + nums[i])
            cur.pop()
            subset(i+1, sum)

        subset(0, 0)
        return res