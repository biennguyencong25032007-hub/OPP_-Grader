class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return 'generic sound'

    def describe(self):
        return f'Tôi là {self.name}, tiếng kêu: {self.make_sound()}'

class Dog(Animal):
    def make_sound(self):
        return 'Gâu!'

class Cat(Animal):
    def make_sound(self):
        return 'Meo!'