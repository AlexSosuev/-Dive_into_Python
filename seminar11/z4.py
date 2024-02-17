# Доработайте прошлую задачу. Добавьте сравнение прямоугольников по площади Должны работать все шесть операций сравнения

from functools import total_ordering

@total_ordering
class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width else length

    def area(self):
        return self.width * self.length

    def __add__(self, other):
        if isinstance(other, Rectangle):
            new_width = self.width + other.width
            new_length = self.length + other.length
            return Rectangle(new_width, new_length)
        raise TypeError

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            if self.width > other.width and self.length > other.length:
                new_width = self.width - other.width
                new_length = self.length - other.length
                return Rectangle(new_width, new_length)
            raise ValueError
        raise TypeError


    def __str__(self):
        return f'{self.length=} {self.width=}'

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        raise TypeError

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        raise TypeError

r1=Rectangle(2,4)
r2=Rectangle(4,4)

print(r1 == r2)
print(r1 >= r2)