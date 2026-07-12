class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if(i != 0 and a == nums[i-1]):
                continue
            if i == len(nums) -2:
                break
            l, r = i+1, len(nums)-1
            # print("a = " + str(a))
            while l < r:
                value = a + nums[l] + nums[r]
                # print("l = " + str(l) + " r = " + str(r) +" value = " + str(value) )

                if value < 0:
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                elif value > 0:
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1
                    
        return res
                
                    