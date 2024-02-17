# Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем. На вход будет подаваться дата в формате "день.месяц.год". Ваша задача - создать программу, которая проверяет, является ли введенная дата корректной или нет.
# Ваша программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна) в зависимости от результата проверки.

def _leap_year(year: int):
    return bool(not year%4 and year%100 or not year%400)


def date_check(input_date: str):
    day, month, year = input_date.split('.')
    day_check = {
        '1': 31,
        '2': 29 if _leap_year(int(year)) else 28,
        '3': 31,
        '4': 30,
        '5': 31,
        '6': 30,
        '7': 31,
        '8': 31,
        '9': 30,
        '10': 31,
        '11': 30,
        '12': 31
    }

    if 0 < int(year) < 10000 and 0 < int(month) < 13 and 0<int(day) <= day_check[month]:
        return True
    return False

date_to_prove = '15.4.2023'
b = date_check(f'{date_to_prove}')
print(b)