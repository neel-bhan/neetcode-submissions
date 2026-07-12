class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, i in enumerate(nums):
            if i in d:
                return [d[i], index]
            d[target - i] = index
        return [0,0]