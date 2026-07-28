class TimeMap:

    def __init__(self):
        self.d= {} #timestamp,key: value
        self.order= defaultdict(list) #key:timestamps

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[(timestamp, key)] = value
        self.order[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        li = self.order[key]
        print(li)
        l, r = 0, len(li) -1
        li.sort()
        res = -1
        while l <= r:
            m = (l+r) // 2
            if li[m] <= timestamp:
                l = m+1
                res = li[m]
            else:
                r = m-1
        return "" if res == -1 else self.d[(res, key)]
        
