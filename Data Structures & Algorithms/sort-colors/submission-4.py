class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0 , len(nums)-1
        index = 0
        while index < len(nums) and index <= j:
            if nums[index] == 0:
                nums[index], nums[i] = nums[i],nums[index]
                i+=1
            if nums[index] == 2:
                nums[index], nums[j] = nums[j], nums[index]
                j-=1
                index-=1
            index +=1
        return nums

            
        