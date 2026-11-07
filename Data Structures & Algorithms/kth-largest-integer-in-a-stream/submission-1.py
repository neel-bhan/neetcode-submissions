class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = []
        for n in nums:
            heapq.heappush(self.h, n)
        while self.h and len(self.h) > k:
            heapq.heappop(self.h)
        self.k = k
        

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        if len(self.h) > self.k:
            heapq.heappop(self.h)
        return self.h[0]
        
