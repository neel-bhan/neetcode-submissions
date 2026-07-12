class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        smaller, larger = nums1, nums2
        if n > m: 
            smaller, larger = larger, smaller
            n, m = m, n
        
        l, r = 0, len(smaller)
        half = (n + m) // 2
        
        while l <= r:
            middle = (l + r) // 2
            lm = half - middle 

            sl = smaller[middle - 1] if middle > 0 else float("-inf")
            sr = smaller[middle] if middle < n else float('inf')
            ll = larger[lm - 1] if lm > 0 else float("-inf")
            lr = larger[lm] if lm < m else float("inf")

            if(sl > lr):
                r = middle - 1
            elif(ll > sr):
                l = middle + 1                 
            else:
                leftMax = max(sl, ll)
                rightMin = min(sr, lr)
                if (n + m) % 2:
                    return rightMin
                return (leftMax + rightMin) / 2