class CountSquares:

    def __init__(self):
        self.c = defaultdict(list)
        self.r = defaultdict(list)
        

    def add(self, point: List[int]) -> None:
        self.c[point[0]].append(point[1])
        self.r[point[1]].append(point[0])

    def count(self, point: List[int]) -> int:

        pr = self.r[point[1]]
        pc = self.c[point[0]]
        li = []
        for cur in pr:
            if cur == point[0]:  # Prevent zero-width squares
                continue
            for i in self.c[cur]:
                li.append((cur, i))

        res = 0
        for row, col in li:
            temp = 0
            for i in pc:
                if i == col:
                    temp += 1
            if col in pc and abs(point[0] - row) == abs(point[1] - col):
                res += temp
        return res