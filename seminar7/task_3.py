# Задание No3
# ✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало.
import os
from random import randint


def get_prod_nick(directory: str = 'sample', random_num_file: str = 'random_file.txt',
                  nick_name_file: str = 'nick_name.txt',
                  res_file: str = 'res_file.txt'):
    if not os.path.exists(directory):
        os.makedirs(directory)
    if not os.path.isfile(os.path.join(directory, random_num_file)) or not os.path.isfile(
            os.path.join(directory, nick_name_file)):
        print('wrong names')
        exit(1)
    with (
        open(os.path.join(directory, random_num_file), 'r', encoding='utf-8') as nu,
        open(os.path.join(directory, nick_name_file), 'r', encoding='utf-8') as ni
    ):
        nums = [int(line.split(' | ')[0]) * float(line.split(' | ')[1]) for line in nu.readlines()]
        nicks = [words.replace('\n', '') for words in ni.readlines()]
    while os.path.exists(os.path.join(directory, res_file)):
        name, extension = os.path.splitext(res_file)
        res_file = f'{name}_{randint(0, 9)}{extension}'
    with open(os.path.join(directory, res_file), 'w', encoding='utf-8') as res:
        for i in range(max(len(nicks), len(nums))):
            res.write(
                nicks[i % len(nicks)].upper() + ' | ' + str(int(nums[i % len(nums)])) + '\n' if nums[i % len(nums)] > 0
                else nicks[i % len(nicks)].lower() + ' | ' + str(abs(nums[i % len(nums)])) + '\n')


if __name__ == '__main__':
    get_prod_nick()
