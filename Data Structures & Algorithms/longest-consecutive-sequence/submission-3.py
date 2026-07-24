class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        cur = 0
        for i in nums:
            cur = 0
            if i-1 in nums:
                continue
            else:
                while i in nums:
                    cur +=1
                    i+=1
            res = max(res, cur)
        return res        