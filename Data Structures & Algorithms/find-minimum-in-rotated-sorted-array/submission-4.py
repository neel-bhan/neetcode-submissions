class Solution:
    def findMin(self, nums: List[int]) -> int:
        #if l > r and m > l: [m:r]
        #if l > r and m < l: [l:m]
        
        l, r= 0, len(nums)-1
        while l <= r:
            m = (l+r) // 2
            if nums[l] > nums[r]:
                if nums[m] >= nums[l]:
                    l = m+1
                else:
                    r = m
            else:
                return nums[l]

