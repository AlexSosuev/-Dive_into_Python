# Задание No2
# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
import os
from random import randint, choice
from string import ascii_lowercase

MIN_LEN_NAME = 4
MAX_LEN_NAME = 7

vowels = ['a', 'o', 'e', 'i', 'u']


def generate_nick_name(count_names: int, directory: str = 'sample', file_name: str = 'nick_name.txt'):
    if count_names:
        if not os.path.exists(directory):
            os.makedirs(directory)
        while os.path.exists(os.path.join(directory, file_name)):
            name, extension = os.path.splitext(file_name)
            file_name = f'{name}_{randint(0, 9)}{extension}'
        with open(os.path.join(directory, file_name), 'w', encoding='utf-8') as f:
            for i in range(count_names):
                f.write(generate_nick(MIN_LEN_NAME, MAX_LEN_NAME) + '\n')


def generate_nick(min_len_name: int, max_len_name: int):
    flag = False
    nick = ''
    nick_len = randint(min_len_name, max_len_name)
    for j in range(nick_len):
        chr = choice(list(ascii_lowercase))
        nick += chr
        if chr in vowels:
            flag = True
    if not flag:
        nick = nick[:-1] + choice(vowels)
    return nick.title()


if __name__ == '__main__':
    generate_nick_name(10)
