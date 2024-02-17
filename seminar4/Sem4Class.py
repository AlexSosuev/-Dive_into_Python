# Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки. Строки нумеруются начиная с единицы. Слова выводятся 
# отсортированными согласно кодировки Unicode. Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

text = "hello beautiful world"
def text_method(text: str):
    my_list = sorted(text.split())
    max_len = 0
    for item in my_list:
        if len(item) > max_len:
            max_len = len(item)
    for i, item in enumerate(my_list, start=1):
        print(i, item.rjust(max_len))

text_method(text)

# Напишите функцию, которая принимает строку текста. Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.

def chars (text):
    new = []
    for i in set(text):
        new.append(ord(i))
    return sorted(new, reverse=True)

print(chars('age 7iy347f347 c37fc3f83rfcfy3'))


# Функция получает на вход строку из двух чисел через пробел. Сформируйте словарь, где ключом будет символ из Unicode, а значением —  целое число. Диапазон пар 
# ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.

def solution(nums: str):
    nums = list(map(int, nums.split()))
    return {chr(num): num for num in range(min(nums), max(nums) + 1)}

print(solution('678 690'))

# Функция получает на вход список чисел. Отсортируйте его элементы in place без использования встроенных в язык сортировок. Как вариант напишите сортировку 
# пузырьком. Её описание есть в википедии.
import random

my_list = [random.randint(1, 10) for x in range(10)]

def buble_sort(my_list):
    n = len(my_list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

print(my_list)
buble_sort(my_list)
print(my_list)

# Функция принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида «10.25%». Вернуть словарь с именем в 
# качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии.

def solution(names, salary, bonus):
    data = list(zip(names, salary, bonus))
    return {item[0]: item[1]*float(item[2].replace('%', ''))/100 for item in data}

print(solution(["ivan", "maxim"], [3000, 4500], ["0.25%", "0.33"]))

# 2-й вариант
# def bonus_calculation(names, base, bonus):
#   result = {}
#   for i in range(len(base)):
#        result[names[i]] = (base[i] * float(bonus[i][:-1])/100)
#   return result

# print(bonus_calculation(["ivan", "maxim"], [3000,4500], ["0.25%", "0.33%"]))

# Функция получает на вход список чисел и два индекса. Вернуть сумму чисел между переданными индексами. Если индекс выходит за пределы списка, сумма 
# считается до конца и/или начала списка.

def summ_between (list, start, finish):
    #start=0 if start<0 else start
    #finish=len(list) if finish>len(list) else finish
    return sum(list[start:finish+1])

print(summ_between([1,2,4,5], -5,7))

# Функция получает на вход словарь с названием компании в качестве ключа и списком с доходами и расходами (3-10 чисел) в качестве значения.
# Вычислите итоговую прибыль или убыток каждой компании. Если все компании прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

companies = {
            "Microsoft":[300, 500, -200.5, -100],
            "IBM":[600, -200, 200.5, 5000],
            "Google":[900, -400, -200.5, -100]
}

def earn_count (my_dict):
    for comp in my_dict:
        if sum(my_dict[comp])<0:
            return False
    return True

print(earn_count (companies))

# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s». Напишите функцию, которая при запуске заменяет содержимое переменных 
# оканчивающихся на s (кроме переменной из одной буквы s) на None. Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

data = [12, 3, 4, 5, 6]
starts = '23:34:10'
s = 'Буква S'
limits = (23, 56)

def solution():
    temp = globals().copy()
    for var, value in temp.item():
        if var.endswith('s') and len(var) > 1:
            globals()[var[:-1]] = value
            globals()[var] = None
solution()