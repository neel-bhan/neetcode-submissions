class MedianFinder:

    def __init__(self):
        self.min = []
        self.max = []

    def addNum(self, num: int) -> None:
        if not self.max:
            heapq.heappush(self.max, - num)
            return
            
        if num >= -self.max[0]:
            heapq.heappush(self.min, num)
        else:
            heapq.heappush(self.max, -num)

        if len(self.max) - len(self.min) > 1:
            heapq.heappush(self.min, -heapq.heappop(self.max))
        elif len(self.min) - len(self.max) >= 1:
            heapq.heappush(self.max, -heapq.heappop(self.min))
            
    def findMedian(self) -> float:
        print(len(self.min))
        print(len(self.max))
        print("next")
        if len(self.min) == len(self.max):
            return (self.min[0] + -self.max[0])/2
        else:
            return -self.max[0]
       

        