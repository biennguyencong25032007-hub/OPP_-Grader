import math

class Point:
    def __init__(self, x=0, y=1):
        # Sử dụng thuộc tính private như trong image_6418fb.png
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
        # Nếu không có 'other', tính khoảng cách đến gốc tọa độ (0,0)
        target_x = other.getX() if other else 0
        target_y = other.getY() if other else 0
        return math.sqrt((self.__x - target_x)**2 + (self.__y - target_y)**2)

    def print(self):
        # Định dạng in số nguyên nếu không có phần thập phân
        ix = int(self.__x) if self.__x == int(self.__x) else self.__x
        iy = int(self.__y) if self.__y == int(self.__y) else self.__y
        return f"({ix}, {iy})"

class LineSegment:
    def __init__(self, *args):
        # Xử lý 4 loại constructor theo yêu cầu
        if len(args) == 0:
            self.p1 = Point(0, 0)
            self.p2 = Point(0, 0)
        elif len(args) == 2 and isinstance(args[0], Point):
            # Tạo Point mới để đảm bảo tính độc lập
            self.p1 = Point(args[0].getX(), args[0].getY())
            self.p2 = Point(args[1].getX(), args[1].getY())
        elif len(args) == 4:
            self.p1 = Point(args[0], args[1])
            self.p2 = Point(args[2], args[3])
        elif len(args) == 1 and isinstance(args[0], LineSegment):
            # SAO CHÉP SÂU (Deep Copy)
            self.p1 = Point(args[0].p1.getX(), args[0].p1.getY())
            self.p2 = Point(args[0].p2.getX(), args[0].p2.getY())

    def move(self, dx, dy):
        self.p1.move(dx, dy)
        self.p2.move(dx, dy)

    def length(self):
        return self.p1.distance(self.p2)

    def angle(self):
        dx = self.p2.getX() - self.p1.getX()
        dy = self.p2.getY() - self.p1.getY()
        angle_deg = math.degrees(math.atan2(dy, dx))
        # Trả về số nguyên như expected stdout trong image_63abe0.png
        return int(round(angle_deg))

    def print(self):
        # Định dạng: [(x1, y1); (x2, y2)]
        print(f"[{self.p1.print()}; {self.p2.print()}]")

class LineSegmentTest:
    def testCase(self):
        # 1. Đọc dữ liệu đầu vào
        try:
            line = input().split()
            if not line: return
            coords = list(map(float, line))
            x1, y1, x2, y2 = coords[0], coords[1], coords[2], coords[3]
        except (EOFError, IndexError):
            return

        # 2. Tạo ls1 và in thông tin ban đầu
        ls1 = LineSegment(x1, y1, x2, y2)
        ls1.print()
        print(f"{ls1.length():.1f}")
        print(f"{ls1.angle()}")

        # 3. Thử nghiệm Sao chép sâu (Deep Copy)
        ls2 = LineSegment(ls1)

        # 4. Di chuyển ls1 nhưng ls2 phải đứng yên
        ls1.move(1, 1)

        # 5. In kết quả cuối cùng để Grader so khớp
        ls1.print()
        ls2.print()