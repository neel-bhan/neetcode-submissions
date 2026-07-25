class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1

        res = 0
        ml,mr = height[0],height[-1]
        while r > l:
            water = 0
            if ml <= mr:
                l+=1
                ml = max(ml, height[l])
                water = min(ml, mr) - height[l]
            else:
                r-=1
                mr = max(mr, height[r])
                water = min(mr, ml) - height[r]
            res += water if water >= 0 else 0
        return res