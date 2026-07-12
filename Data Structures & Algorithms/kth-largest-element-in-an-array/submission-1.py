class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        heapq.heapify(res)
        for i in nums:
            if len(res) <k:
                heapq.heappush(res,i)
            else:
                heapq.heappush(res, i)
                heapq.heappop(res)
            
        res.sort()
        print(res)
        return res[0]