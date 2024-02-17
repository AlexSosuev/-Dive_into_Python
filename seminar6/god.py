# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY Функция возвращает истину, если дата может 
# существовать или ложь, если такая дата невозможна. Для простоты договоримся, что год может быть в диапазоне [1, 9999]. Весь период 
# (1 января 1 года -31 декабря 9999 года) действует Григорианский календарь. Проверку года на високосность вынести в отдельную защищённую функцию.

def _leap_year(year: int):
    return bool(not year%4 and year%100 or not year%400)


def date_check(input_date: str):
    day, month, year = input_date.split('.')
    day_check = {
        '01': 31,
        '02': 29 if _leap_year(int(year)) else 28,
        '03': 31,
        '04': 30,
        '05': 31,
        '06': 30,
        '07': 31,
        '08': 31,
        '09': 30,
        '10': 31,
        '11': 30,
        '12': 31
    }

    if 0 < int(year) < 10000 and 0 < int(month) < 13 and 0<int(day) <= day_check[month]:
        return True
    return False

print(date_check('22.12.2099'))
print(date_check('29.02.2017'))
print(date_check('29.02.2016'))
print(date_check('31.04.2099'))