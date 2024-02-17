# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
from z3 import Human
from random import randint

class Employee(Human):
    __id_list = []
    __SEP = 7
    __ID_START = 100000

    def __init__(self, name, surname, patronymic, age, id_number):
        super().__init__(name, surname, patronymic, age)
        if len(str(id_number)) != 6:
            self.id_number = randint(100_000, 999_999)
        else:
            self.id_number = id_number

    def secure_level(self):
        return sum((int(i) for i in str(self.id_number))) % 7


if __name__ == '__main__':
    staff_1 = Employee('Paul', 'Jonthon', 'Junior', 45, 1674846)    
    print(f"{staff_1.secure_level()=  }")
   