# 📌 Доработайте класс прямоугольник из прошлых семинаров. 
# 📌 Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений (отрицательных). 
# 📌 Используйте декораторы свойств.

class Rectangle:
    __slots__ = ('_width', '_length')
    
    def __init__(self, length, width = None):
        self._length = length
        self._width = width if width else length

    def perimetr(self):
        return 2 * self._length + 2 * self._width

    def area(self):
        return self._length * self._width


    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @length.setter
    def length(self, value):
        if value > 0:
            self._length = value
        else:
            raise ValueError('Размер не может быть отрицательным')

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError('Размер не может быть отрицательным') 


rect1 = Rectangle(3, 4)
rect1.length = 4
# rect1.width = -4 
print(rect1.length)