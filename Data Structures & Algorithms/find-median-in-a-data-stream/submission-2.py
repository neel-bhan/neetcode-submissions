class MedianFinder:

    def __init__(self):
        self.min = []
        self.max = []

    def addNum(self, num: int) -> None:
        if self.min and num > self.min[0]:
            heapq.heappush(self.min, num)
        else:
            heapq.heappush(self.max, -num)
        if len(self.min) > len(self.max) + 1:
            val = -heapq.heappop(self.min)
            heapq.heappush(self.max, val)
        if len(self.max) > len(self.min) + 1:
            val = -heapq.heappop(self.max)
            heapq.heappush(self.min, val)
        

    def findMedian(self) -> float:
        if len(self.min) > len(self.max):
            return self.min[0]
        if len(self.max) > len(self.min):
            return -self.max[0]
        return (self.min[0] - self.max[0]) /2

        