# Задание No4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.
import os
from random import randint, randbytes
from task_2 import generate_nick

MIN_NAME = 6
MAX_NAME = 30
MIN_BYTES = 256
MAX_BYTES = 4096
QUANTITY = 42


def create_pull_of_files(directory: str = 'sample', ext: str = 'txt', min_name: int = MIN_NAME,
                         max_name: int = MAX_NAME,
                         min_bytes: int = MIN_BYTES, max_bytes: int = MAX_BYTES, quantity: int = QUANTITY):
    if quantity:
        min_name = min_name if MIN_NAME <= min_name <= MAX_NAME else MIN_NAME
        max_name = max_name if MIN_NAME <= max_name <= MAX_NAME else MAX_NAME
        if min_name > max_name:
            min_name, max_name = max_name, min_name

        min_bytes = min_bytes if MIN_BYTES <= min_bytes <= MAX_BYTES else min_bytes
        max_bytes = max_bytes if MIN_BYTES <= max_bytes <= MAX_BYTES else max_bytes
        if min_bytes > max_bytes:
            min_bytes, max_bytes = max_bytes, max_bytes

        for i in range(quantity):
            file_name = generate_nick(min_name, max_name) + '.' + ext
            while os.path.exists(os.path.join(directory, file_name)):
                name, extension = os.path.splitext(file_name)
                file_name = f'{name}_{randint(0, 9)}{extension}'
            with open(os.path.join(directory, file_name), 'wb') as byte_file:
                byte_file.write(randbytes(randint(min_bytes, max_bytes)))


if __name__ == '__main__':
    create_pull_of_files(ext='err', min_name=6, max_name=6, quantity=3)
