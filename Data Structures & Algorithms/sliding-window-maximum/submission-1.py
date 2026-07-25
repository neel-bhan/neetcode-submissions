class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        for i in range(k-1):
            heapq.heappush(h, (-nums[i], i))
        r = k-1
        res = []
        for l in range(len(nums)-k+1):
            heapq.heappush(h, (-nums[r], r))
            r+=1
            cur = heapq.heappop(h)
            while not cur[1] in range(l, r):
                cur = heapq.heappop(h)
            heapq.heappush(h,cur)
            res.append(-cur[0])
        return res
