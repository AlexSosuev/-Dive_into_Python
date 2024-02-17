# Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который содержит уникальные (без повтора) элементы исходного списка. Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.
my_list = [1,2,3,4,2,3,4]
print(list(set(my_list)))

new_list=[]
for i in my_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)

# Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже: Целое положительное число; Вещественное положительное или отрицательное число; Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква; Строку в нижнем регистре в остальных случаях

user = input('Введите данные:')
if user.isdigit():
    print('Integer')
elif user.count(".")== 1 and user.replace(".","").replace("-","").isdigit():
    print("Float")
elif any([sym.isupper() for sym in user]):
    print("Upper")
else:
    print("Lower")

# Создайте вручную кортеж содержащий элементы разных типов. Получите из него словарь списков, где: ключ — тип элемента, значение — список элементов данного типа.
    
text = {12, "my", "our", (1, 3, "d"), True, False, 45.3, None, -87, [1,2,3]}
new_dict = []
for item in text:
    t = type(item)
    if t in new_dict:
        new_dict[t].append(item)
    else:
        new_dict[t] = [item]
print(new_dict)

# Создайте вручную список с повторяющимися элементами. Удалите из него все элементы, которые встречаются дважды.

my_list = [1, 2, 3, 3, 2, 4, 3]

for i in set(my_list):
    if my_list.count(i) == 2:
            my_list.remove(i)
            my_list.remove(i)
print(my_list)

# Создайте вручную список с повторяющимися целыми числами. Сформируйте список с порядковыми номерами нечётных элементов исходного списка. Нумерация начинается с единицы.
my_list1 = [1, 2, 3, 3, 2, 4, 3]
new_list =[]
for i in range(len(my_list1)):
    if my_list1[i] % 2 != 0:
        new_list.append(i+1)
print(new_list)

# Пользователь вводит строку текста. Вывести каждое слово с новой строки. Строки нумеруются начиная с единицы. Слова выводятся отсортированными согласно кодировки Unicode. Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

my_str = input("Введите строку: ").split()
my_str.sort()
print(my_str)

longstr = len(max(my_str, key=len))
for num, element in enumerate(my_str, 1):
    print(f"{num} {element:>{longstr}}")

# Пользователь вводит строку текста. Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним. Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке. Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.

my_str1 = input("Введите строку: ")
my_set = set(my_str1)
my_dict1 = {}
# count = 0
# for i in my_set:
#     for j in range(len(my_str1)):
#         if my_str1[j] == i:
#             count += 1
#     my_dict1[i] = count
#     count = 0
# print(my_dict1)

# for item in my_set:
#     my_dict1.setdefault(item, my_str1.count(item))
# print(my_dict1)

for item in my_str1:
    my_dict1[item] = my_dict1.get(item, 0) + 1
print(my_dict1)

# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы: Какие вещи взяли все три друга Какие вещи уникальны, есть только у одного друга Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

friends_stuff = {
    'Олег': ('палатка', 'топор','еда','пиво'),
    'Игорь': ('палатка', 'вилка','вода','пиво'),
    'Гусь': ('палатка', 'топор','вода','пиво'),
    'Стоун': ('палатка', 'топор','вода','энергетик')
}

set1 = set()
for k in friends_stuff:
    if not set1:
        set1 = set(friends_stuff[k])
    else:
        set1 &= set(friends_stuff[k])
print("Вещи друзей:", set1)

my_tuple = friends_stuff.keys()

my_set = set()
for friends in my_tuple:
    my_set = set(friends_stuff[friends])
    for other_friends in [i for i in my_tuple if i != friends]:
        my_set = my_set - set(friends_stuff[other_friends])
    if my_set:
        print(f"Вещи уникальны, есть только у {friends}:", *my_set)

for friends in my_tuple:
    my_set = set()
    to_remove = set(friends_stuff[friends])
    for other_friends in [i for i in my_tuple if i != friends]:
        if not my_set:
            my_set = set(friends_stuff[other_friends])
        else:
            my_set = my_set & set(friends_stuff[other_friends])
    my_set -= to_remove
    if my_set:
        print(f"{friends} не взял \"t {my_set}")