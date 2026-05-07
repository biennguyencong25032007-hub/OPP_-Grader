import math
import sys

class TuLanh:
    def __init__(self, nhanhieu, maso, nuocsx, tkdien, dungtich, gia):
        self.__nhanhieu = nhanhieu
        self.__maso = maso
        self.__nuocsx = nuocsx
        self.__tkdien = tkdien
        self.__dungtich = dungtich
        self.__gia = gia

    def print(self):
        tiet_kiem = "Có" if self.__tkdien else "Không"
        print(f"Nhãn hiệu: {self.__nhanhieu}")
        print(f"Mã số: {self.__maso}")
        print(f"Nước SX: {self.__nuocsx}")
        print(f"T/K điện: {tiet_kiem}")
        print(f"Dung tích: {self.__dungtich}L")
        print(f"Giá: {self.__gia}VNĐ")

class TuLanhTest:
    def testCase(self):
        try:
            line1 = sys.stdin.readline().strip()
            line2 = sys.stdin.readline().strip()
            
            parts1 = line1.split('|')
            tu1 = TuLanh(parts1[0], parts1[1], parts1[2], parts1[3] == 'True', int(parts1[4]), int(parts1[5]))
            
            parts2 = line2.split('|')
            tu2 = TuLanh(parts2[0], parts2[1], parts2[2], parts2[3] == 'True', int(parts2[4]), int(parts2[5]))
            
            SEP = '= = = = = = = ='
            
            print(SEP)
            tu1.print()
            print(SEP)
            tu2.print()
            print(SEP)
            
        except Exception:
            pass