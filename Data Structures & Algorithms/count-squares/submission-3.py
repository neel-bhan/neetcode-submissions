class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.point = []
        

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        self.point.append(point)
    def count(self, point: List[int]) -> int:

        px, py = point
        res =0 
        for x, y in self.point:
            if (abs(px -x) != abs(py-y)) or x == px or y == py:
                continue
            res += self.points[(x, py)] * self.points[(px, y)]
        return res