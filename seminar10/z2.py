# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат

class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        if width:
            self.width = width
        else:
            self.width = length

    def get_perimeter(self):
        return 2 * (self.width + self.length)

    def get_square(self):
        return self.width * self.length


if __name__ == '__main__':
    first = Rectangle(5, 10)
    second = Rectangle(5)
    print(first.get_perimeter())
    print(first.get_square())
    print(second.get_perimeter())
    print(second.get_square())