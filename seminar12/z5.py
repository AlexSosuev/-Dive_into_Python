# 📌 Изменяем класс прямоугольника. 
# 📌 Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.

class SiteValidate:
    def __init__(self, min_value: float = None, max_value: float = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'{value} is lesser than {self.min_value}')
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f'{value} is greater than {self.max_value}')


class Rectangle:
    sida_a = SiteValidate(1, 20)
    side_b = SiteValidate(1, 15)

    def __init__(self, a, b):
        self.sida_a = a
        self.side_b = b 

    def __str__(self):
        return f'Прямоугольник {self.sida_a} x {self.side_b}'


rect_1 = Rectangle(20, 20)
print(rect_1)