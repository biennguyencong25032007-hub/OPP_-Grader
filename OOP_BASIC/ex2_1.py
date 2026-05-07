import math

# Lớp Point (Kế thừa hoặc viết lại từ bài 1.1)
class Point:
    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def read(self):
        # Đọc dữ liệu từ stdin theo định dạng "x y"
        try:
            line = input().split()
            if len(line) >= 2:
                self.x = float(line[0])
                self.y = float(line[1])
        except EOFError:
            pass

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance(self):
        # Tính khoảng cách từ điểm hiện tại đến gốc tọa độ (0, 0)
        return math.sqrt(self.x**2 + self.y**2)

    def print(self):
        # In tọa độ theo định dạng (x, y), nếu là số nguyên thì in số nguyên
        # Ép kiểu int nếu x, y là số nguyên để khớp với format mẫu
        out_x = int(self.x) if self.x == int(self.x) else self.x
        out_y = int(self.y) if self.y == int(self.y) else self.y
        print(f"({out_x}, {out_y})")

# Lớp PointTest theo yêu cầu bài 1.2
class PointTest:
    def testCase(self):
        # 1. Tạo p1 = Point() mặc định và in ra
        p1 = Point()
        p1.print()

        # 2. Tạo p2 = Point(), đọc tọa độ từ stdin và in ra
        p2 = Point()
        p2.read()
        p2.print()

        # 3. Di chuyển p2 thêm (1, 1) và in ra
        p2.move(1, 1)
        p2.print()

        # 4. Tính và in khoảng cách từ p2 mới đến gốc tọa độ O
        # Lưu ý: Grader yêu cầu in số thực (VD: 5.0 hoặc 0.0)
        dist = p2.distance()
        print(f"{dist:.1f}" if dist == int(dist) else dist)

# Lưu ý: Không viết main hoặc if __name__ == "__main__" khi nộp bài