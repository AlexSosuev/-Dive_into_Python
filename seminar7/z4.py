# Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры: расширение минимальная длина 
# случайно сгенерированного имени, по умолчанию 6 максимальная длина случайно сгенерированного имени, по умолчанию 30 минимальное число 
# случайных байт, записанных в файл, по умолчанию 256 максимальное число случайных байт, записанных в файл, по умолчанию 4096 количество 
# файлов, по умолчанию 42 Имя файла и его размер должны быть в рамках переданного диапазона.

from random import randbytes, randint, choice
from string import ascii_lowercase

MIN_NAME = 6
MAX_NAME = 30
MIN_SIZE = 256
MAX_SIZE = 4096
COUNT = 42


def gen_files(ext: str, min_name: int = MIN_NAME, max_name: int = MAX_NAME, 
              min_size: int = MIN_SIZE, max_size: int = MAX_SIZE, count: int = COUNT):
    count = count if 0 < count <= COUNT else randint(1, COUNT)
    for _ in range(count):
        cur_min_name = min_name if (MIN_NAME <= min_name < MAX_NAME) else MIN_NAME
        cur_max_name = max_name if (MIN_NAME < max_name <= MAX_NAME) else MAX_NAME
        cur_min_size = min_size if (MIN_SIZE <= min_size < MAX_SIZE) else MIN_SIZE
        cur_max_size = max_size if (MIN_SIZE < max_size <= MAX_SIZE) else MAX_SIZE
        name = ''
        for _ in range(min([cur_min_name, cur_max_name]), max([cur_min_name, cur_max_name]) + 1):
            name += choice(list(ascii_lowercase))
        name += '.' + ext[:3]
        with open(name, 'wb') as file:    
            file.write(randbytes(randint(cur_min_size, cur_max_size)))