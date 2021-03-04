
class Bbox:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

    def __repr__(self):
        return f"(({self.x0}, {self.y0}), ({self.x1}, {self.y1}))"

    def __add__(self, other):
        x0 = self.x0 + other.x0
        y0 = self.y0 + other.y0
        x1 = self.x1 + other.x1
        y1 = self.y1 + other.y1
        return Bbox(x0, y0, x1, y1)

    def __eq__(self, other):
        return all((self.x0 == other.x0, self.y0 == other.y0, self.x1 == other.x1, self.y1 == other.y1))


bbox_1 = Bbox(1,2,4,7)
bbox_2 = Bbox(1,2,4,7)
bbox_3 = bbox_1 + bbox_2  # полиморфизм
print(bbox_3)
print(bbox_1 == bbox_2)
