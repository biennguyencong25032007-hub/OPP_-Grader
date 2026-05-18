class Temperature:
    def __init__(self, celsius: float):
        self.celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = float(value)

    @property
    def fahrenheit(self) -> float:
        return float(self._celsius * 9 / 5 + 32)

    @fahrenheit.setter
    def fahrenheit(self, value: float):
        c_value = (value - 32) * 5 / 9
        self.celsius = c_value