class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        l, r = 0, len(nums) - 1
        while l <= r:
            piv = nums[r]
            cur = l 
            for i in range(l, r):
                if nums[i] <= piv:
                    nums[cur], nums[i] = nums[i], nums[cur]
                    cur += 1
            nums[cur], nums[r] = nums[r], nums[cur]
            if cur == k:
                return nums[cur]
            else:
                if k > cur:
                    l = cur + 1
                else:
                    r = cur -1
        return -1            

            

