# Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.
import os
from random import randint, uniform

MIN = -1000
MAX = 1000


def add_random_pairs(lines: int, directory: str = 'sample', file_name: str = 'random_file.txt'):
    if lines:
        if not os.path.exists(directory):
            os.makedirs(directory)
        while os.path.exists(os.path.join(directory, file_name)):
            name, extension = os.path.splitext(file_name)
            file_name = f'{name}_{randint(0, 9)}{extension}'
        with open(os.path.join(directory, file_name), 'w', encoding='utf-8') as file:
            for line in range(lines):
                file.write(f'{randint(MIN, MAX)} | {uniform(MIN, MAX)} \n')


if __name__ == '__main__':
    add_random_pairs(10)
