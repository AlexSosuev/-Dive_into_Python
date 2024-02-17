# Дорабатываем класс прямоугольник из прошлого семинара. Добавьте возможность сложения и вычитания. При этом должен создаваться новый экземпляр прямоугольника. Складываем и вычитаем периметры, а не длинну и ширину. При вычитании не допускайте отрицательных значений.

class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        if width:
            self.width = width
        else:
            self.width = length

    def __add__(self, other):
        if isinstance(other, Rectangle):
            new_width = self.width + other.width
            new_length= self.length + other.length
            return Rectangle(new_width, new_length)
        raise TypeError
    
    def __sub__(self, other):
        if isinstance(other, Rectangle):
            if self.width > other.width and self.length > other.length:
                new_width = self.width - other.width
                new_length= self.length - other.length
                return Rectangle(new_width, new_length)
            raise ValueError
        raise TypeError
    
    def __str__(self):
        return f'{self.length=} {self.width=}'

r1 = Rectangle(2, 4)
r2 = Rectangle(3, 4)

print(r1 + r2)
print(r1 - r2)