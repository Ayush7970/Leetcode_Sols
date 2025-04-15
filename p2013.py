class DetectSquares:

    def __init__(self):

        self.pts_count = defaultdict(int)
        self.list = []

    def add(self, point: List[int]) -> None:
        self.pts_count[tuple(point)] += 1
        # self.list.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        x2, y2 = point
        for (x1, y1), count in list(self.pts_count.items()):
            print(x1, y1)
            if abs(x1 - x2) != abs(y1 - y2) or x1 == x2 or y1 == y2:
                continue
            
            res += count * self.pts_count[(x1, y2)] * self.pts_count[(x2, y1)]
        return res

        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)