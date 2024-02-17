# Дорабатываем задачу 4.
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить. В этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
# *Научите функцию распознавать не только текстовое названия дня недели и месяца, но и числовые, т.е не мая, а 5.
import datetime
import argparse

DAYS = ['понедельник', 'вторник', 'среда', 'четверг',
'пятница', 'суббота', 'воскресенье']

parser = argparse.ArgumentParser(description='Find date')
parser.add_argument('-date', metavar='date', type=str, nargs='*', help='Enter a number of weekday in month')
parser.add_argument('-day', metavar='day', type=int, default=datetime.datetime.now().weekday(),
help='Enter a number of weekday in month')
parser.add_argument('-dow', metavar='dow', type=str, default=DAYS[datetime.datetime.now().weekday()],
help='Enter a name of weekday')
parser.add_argument('-mon', metavar='mon', type=str, default=datetime.datetime.now().month, help='Enter a month name')
args = parser.parse_args()
print(args.day, args.dow, args.mon)


def _is_leap_year(year):
    return bool(not year % 4 and year % 100 or not year % 400)


def convert_string_to_date(day_number, day_name, month_name):
    current_year = datetime.datetime.now().year
    weekday_names = ['понедельник', 'вторник', 'среда', 'четверг',
    'пятница', 'суббота', 'воскресенье']

    month_names = {
    'январ': (31, 1), 'феврал': (29 if _is_leap_year(current_year) else 28, 2),
    'мар': (31, 3), 'апрел': (30, 4), 'ма': (31, 5), 'июн': (30, 6),
    'июл': (31, 7), 'авгус': (31, 8), 'сентябр': (30, 9),
    'октябр': (31, 10), 'ноябр': (30, 11), 'декабр': (31, 12)}

    try:
        first_day = datetime.datetime.strptime(f'1 {month_names[month_name[:-1]][1]} {current_year}',
        "%d %m %Y").weekday()
    except:
        raise ValueError
    count = 0
    weekday_names = weekday_names[first_day:] + weekday_names[:first_day]
    current_month = month_names[[month for month in month_names if month_name[:-1] in month][0]]


    while count < month_names[month_name[:-1]][0]:
        if day_name == weekday_names[count % 7]:
            day_number -= 1
            if not day_number:
                break
        count += 1
    else:
        raise ValueError
    print(count+1)
    return count + 1

if __name__ == '__main__':
    convert_string_to_date(args.day, args.dow, args.mon)