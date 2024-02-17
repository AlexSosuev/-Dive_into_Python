# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

file_path = "C:/Users/User/Documents/example.txt"

import os
def get_file_info(file_path):
    file_dir, file_name = os.path.split(file_path)
    if file_dir:
        file_dir += '/'
    file_name, file_ext = os.path.splitext(file_name)
    return file_dir, file_name, file_ext