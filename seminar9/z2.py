# Дорабатываем задачу 1. Превратите внешнюю функцию в декоратор. Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10]. Если не входят, вызывать функцию со случайными числами из диапазонов.

from random import randint as ri
from z3 import json_decor
from z4 import deco_with_params
from functools import wraps

MIN_LIMIT = 1
MAX_LIMIT = 100
MIN_COUNT = 1
MAX_COUNT = 10

def guess_rules(func):
    @wraps(func)
    def inner(number, count):
        user_number = number if MIN_LIMIT <= number <= MAX_LIMIT else ri(MIN_LIMIT,MAX_LIMIT)
        user_count = count if MIN_COUNT <= count <= MAX_COUNT else ri(MIN_COUNT,MAX_COUNT)
        return func(user_number, user_count)
    return inner

@deco_with_params(3)
@json_decor
@guess_rules
def guess_game(user_number, user_count):
    while user_count:
        guess_num = int(input(f'Угадайте число от {MIN_LIMIT} до {MAX_LIMIT}'))
        if guess_num == user_number:
            print(f'Ура, тыпобедил! Это число {user_number}') 
            return f'Победа! {user_number} {user_count}'
        elif guess_num < user_number:
            print('Загаданное число больше!')
        else:
            print('Загаданное число меньше!')
        user_count -= 1
    print(f'Увы! Ты проиграл! это было число {user_number}')   
    return f'Проиграл! {user_number} {user_count}' 


if __name__ == '__main__':
    game = guess_game(65, 7)
    game()