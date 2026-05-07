import math

class Point:
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y

    def getX(self): return self.__x
    def getY(self): return self.__y

    def read(self):
        try:
            line = input().split()
            if len(line) >= 2:
                self.__x, self.__y = float(line[0]), float(line[1])
        except EOFError:
            pass

    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def distance(self, other=None):
        target_x = other.getX() if other else 0
        target_y = other.getY() if other else 0
        return math.sqrt((self.__x - target_x)**2 + (self.__y - target_y)**2)

    def print(self):
        ix = int(self.__x) if self.__x == int(self.__x) else self.__x
        iy = int(self.__y) if self.__y == int(self.__y) else self.__y
        return f"({ix}, {iy})"

class LineSegment:
    def __init__(self, *args):
        if len(args) == 0:
            self.p1 = Point(0, 0)
            self.p2 = Point(0, 0)
        elif len(args) == 2 and isinstance(args[0], Point):
            self.p1 = Point(args[0].getX(), args[0].getY())
            self.p2 = Point(args[1].getX(), args[1].getY())
        elif len(args) == 4:
            self.p1 = Point(args[0], args[1])
            self.p2 = Point(args[2], args[3])
        elif len(args) == 1 and isinstance(args[0], LineSegment):
            self.p1 = Point(args[0].p1.getX(), args[0].p1.getY())
            self.p2 = Point(args[0].p2.getX(), args[0].p2.getY())

    def length(self):
        return self.p1.distance(self.p2)

    def angle(self):
        dx = self.p2.getX() - self.p1.getX()
        dy = self.p2.getY() - self.p1.getY()
        angle_rad = math.atan2(dy, dx)
        angle_deg = math.degrees(angle_rad)
        return int(round(angle_deg))

    def print(self):
        print(f"[{self.p1.print()}; {self.p2.print()}]")

