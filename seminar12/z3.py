# 📌 Создайте класс-генератор. 
# 📌 Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step. 
# 📌 Если переданы два параметра, считаем step=1. 
# 📌 Если передан один параметр, также считаем start=1.

class Factorial:
    def __init__(self, *args):
        data = args[:3]
        self.start, self.step = 1, 1
        if len(data) == 1:
            self.stop = data[0]
        elif len(data) == 2:
            self.start, self.stop = data
        else:
            self.start, self.stop, self.step = data
        self.data = [*range(self.start, self.stop + 1, self.step)]
        self.value = 1
    
    def _get_fact(self, limit):
        fact = 1
        for i in range(1, limit + 1):
            fact *= i
        self.value = fact
        return fact

    def __iter__(self):
        return self

    def __next__(self):
        if self.data:
            return self._get_fact(self.data.pop(0))
        raise StopIteration
    
    def __str__(self):
        return str(self.value)

if __name__ == '__main__':
    factorial_gen = Factorial(5, 10, 3)
    for i in factorial_gen:
        print(i)