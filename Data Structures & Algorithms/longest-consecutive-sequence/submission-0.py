class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for i in s:
            if i - 1 not in s:
                cur = 1
                num = i
                while num + 1 in s:
                    cur += 1
                    num += 1
                res= max(res, cur)
        return res


        