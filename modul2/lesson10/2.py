import abc


class Figure(abc.ABC):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"Класс Figure. Стороны: {self.a}, {self.b}"

class GetSquraMixin:
    def get_square(self):
        return self.a * self.b


class Rectangle(GetSquraMixin, Figure):

    def __str__(self):
        return f"Класс Rectangle. Стороны: {self.a}, {self.b}"


class Square(GetSquraMixin, Figure):
    def __init__(self, a):
        super().__init__(a, a)

    def __str__(self):
        return f"Класс Square. Стороны: {self.a}, {self.b}"


square = Square(10)
print(square)

rect = Rectangle(10, 20)
print(rect)
