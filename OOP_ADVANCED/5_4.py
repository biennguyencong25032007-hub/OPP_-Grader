from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Phương thức trừu tượng tính diện tích."""
        pass

class Circle(Shape):
    def __init__(self, r: int):
        self.r = r

    def area(self) -> float:
        return float(math.pi * self.r * self.r)

class Rectangle(Shape):
    def __init__(self, w: int, h: int):
        self.w = w
        self.h = h

    def area(self) -> float:
        return float(self.w * self.h)