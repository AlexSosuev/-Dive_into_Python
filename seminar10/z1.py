# Создайте класс окружность. Класс должен принимать радиус окружности при создании экземпляра. 
# У класс должно быть два метода, возвращающие длину окружности и ее площадь
import math

class Circle:
    def __init__(self, rad):
        self.rad = rad

    def lenght(self):
        return 2*math.pi*self.rad

    def square(self):
        return math.pi*self.rad**2

if __name__ == "__main__":
    p1 = Circle(5)
    print(f'Длина окружности - {p1.lenght()}')
    print(f'Площадь окружности - {p1.square()}')