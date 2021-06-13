import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, point2):
        return math.sqrt((self.x - point2.x) ** 2 + (self.y - point2.y) ** 2)


class Polygon:
    def __init__(self, points=None):
        points = points if points else []
        self.vertices = []
        for point in points:
            if isinstance(point, tuple):
                point = Point(*point)
            self.vertices.append(point)

    def add_point(self, point):
        self.vertices.append(point)

    def perimeter(self):
        points = self.vertices + [self.vertices[0]]
        perimeter = 0
        for i in range(len(self.vertices)):
            perimeter += points[i].distance(points[i + 1])
        return perimeter


if __name__ == '__main__':
    square = Polygon()
    square.add_point(Point(1, 1))
    square.add_point(Point(1, 2))
    square.add_point(Point(2, 2))
    square.add_point(Point(2, 1))
    print(square.perimeter())