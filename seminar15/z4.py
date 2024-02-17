# Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.

import datetime


def _is_leap_year(year):
    return bool(not year % 4 and year % 100 or not year % 400)


def convert_string_to_date(text):
    current_year = datetime.datetime.now().year
    weekday_names = ['понедельник', 'вторник', 'среда', 'четверг',
    'пятница', 'суббота', 'воскресенье']
    month_names = {
    'январ': (31, 1), 'феврал': (29 if _is_leap_year(current_year) else 28, 2),
    'мар': (31, 3), 'апрел': (30, 4), 'ма': (31, 5), 'июн': (30, 6),
    'июл': (31, 7), 'авгус': (31, 8), 'сентябр': (30, 9),
    'октябр': (31, 10), 'ноябр': (30, 11), 'декабр': (31, 12)}
    try:
        parts = text.split()
        day_number = int(''.join([i for i in parts[0] if i.isdigit()]))
        day_name = parts[1]
        month_name = parts[2]

        first_day = datetime.datetime.strptime(f'1 {month_names[month_name[:-1]][1]} {current_year}',
        "%d %m %Y").weekday()
    except:
        raise ValueError
    count = 0
    weekday_names = weekday_names[first_day:] + weekday_names[:first_day]

    while count < month_names[month_name[:-1]][0]:
        if day_name == weekday_names[count % 7]:
            day_number -= 1
            if not day_number:
                break
        count += 1
    else:
        raise ValueError

    return count + 1
    
text_1 = '1-й четверг ноября'
text_2 = '3-я среда мая'
print(convert_string_to_date(text_1))
print(convert_string_to_date(text_2))