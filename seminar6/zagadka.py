# Создайте модуль с функцией внутри. Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание. 
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

# Добавьте в модуль с загадками функцию, которая хранит словарь списков. Ключ словаря -загадка, значение -список с отгадками. Функция в цикле 
# вызывает загадывающую функцию, чтобы передать ей все свои загадки.

# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана). Функция 
# формирует словарь с информацией о результатах отгадывания. Для хранения используйте защищённый словарь уровня модуля. Отдельно напишите функцию, 
# которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде. Для формирования результатов используйте генераторное выражение.

from random import randint, choice
_dict_protect = dict()

def puzzle(puzle_text: str, variant: list[str], tries: int) -> int:
    print(puzle_text)
    variant_v = list(map(lambda x: x.lower(), variant))
    num  = 0
    while num < tries:
        user_input = input('Введите вариант ответа').lower()
        if user_input in variant_v:
            num += 1
            return num
        else:
            print('Не угадали')
        num += 1
    return 0

def puzzle_solut(count: 2):
    dict_puzzle = {
        'Зимой и летом одним цветом', ['ель','сосна','пихта'],
        'Висит груша нельзя скушать', ['лампа', 'лампочка'],
        'Не лает, не кусает в дом не пускает', ['замок', 'гусь']
    }
    count = count if count < len(dict_puzzle) else len(dict_puzzle)
    for _ in range(count):
        cur_puzzle = choice(list(dict_puzzle))
        cur_value = dict_puzzle.pop(cur_puzzle)
        result = puzzle(cur_puzzle, cur_value, randint(1, 3))
        puzzle_count(cur_puzzle, result)

def puzzle_count(guess_text: str, guess_try: int):
    _dict_protect[guess_text] = guess_try

def puzzle_count_print():
    for guess_text, guess_count in _dict_protect.items():
        print(f'Загадку {guess_text} ' + (f'угадали с попытки {guess_count}' if guess_count else 'не угадали'))