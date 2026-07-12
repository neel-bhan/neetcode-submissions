class TimeMap:

    def __init__(self):
        self.pairs = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.pairs:
            self.pairs[key].append((value, timestamp))
        else:
            self.pairs[key] = [(value, timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.pairs:
            search = self.pairs[key]
        else:
            return ""
        ret = -1
        l,r = 0, len(search) - 1
        index = -1
        while l <= r:
            m = (l + r) // 2
            if search[m][1] > timestamp:
                r = m - 1 
            else:
                if(search[m][1] >= ret):
                    ret = search[m][1]
                    index = m
                l = m + 1
        if index == -1:
            return ""
        else:
            return search[index][0]
