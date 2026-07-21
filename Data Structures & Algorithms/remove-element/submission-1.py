class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = 0
        for i in nums:
            if val != i:
                nums[res] = i
                res += 1
                
        return res