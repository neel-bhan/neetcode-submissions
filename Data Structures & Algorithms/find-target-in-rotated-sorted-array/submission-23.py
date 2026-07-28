class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        i = 0
        while l <= r:
            if i == 10:
                break
            i+=1
            print("start")
            print(l, r)
            m = (l+r) // 2
            print("m" + str(nums[m]))
            if nums[l] > nums[r] :
                print(target < nums[l] and nums[m] > nums[l])
                if nums[m] == target:
                    return m
                elif (target > nums[m] and nums[m] >= nums[l])or (target < nums[l] and nums[m] >= nums[l]) or (target > nums[m] and target <= nums[r]):
                    l = m+1
                elif target > nums[r] or target < nums[m]:
                    r = m-1
            else:
                if target > nums[m]:
                    l= m+1
                elif target < nums[m]:
                    r = m-1
                else:
                    return m
            print("end")
            print(l, r)
        return -1
                
        