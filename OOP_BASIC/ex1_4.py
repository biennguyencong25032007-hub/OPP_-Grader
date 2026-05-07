import math

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