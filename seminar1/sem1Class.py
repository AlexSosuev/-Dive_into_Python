# Напишите программу, которая запрашивает год и проверяет его на високосность. Распишите все возможные проверки в цепочке elif. Откажитесь от магических чисел. Обязательно учтите год ввода Григорианского календаря. В коде должны быть один input и один print.

# in_year = int(input("Введите год: "))
# YEAR1 = 4
# YEAR2 = 100
# YEAR3 = 400
# result = in_year % YEAR1 == 0 and in_year % YEAR2 != 0 or in_year % YEAR3 == 0
# print('Високосный' if result else 'Невисокосный')

# Пользователь вводит число от 1 до 999. Используя операции с числами сообщите что введено: цифра, двузначное число или трёхзначное число. Для цифры верните её квадрат, например 5 - 25. Для двузначного числа произведение цифр, например 30 - 0. Для трёхзначного числа его зеркальное отображение, например 520 - 25. Если число не из диапазона, запросите новое число. Откажитесь от магических чисел. В коде должны быть один input и один print

# while True:
#     num = int(input("Введите число (1-999): "))
#     if num in range(1, 1000):
#         if num < 10:
#             result = num ** 2
#         elif num < 100:
#             result = (num % 10) * (num // 10)
#         else:
#             ones = num % 10
#             hundred = num // 100
#             dosens = (num % 100) // 10
#             result = ones * 100 + dosens * 10 + hundred
#         break
    
# print(result)

# Нарисовать вконсоли елку, спросив у пользователя количество рядов
# SPACE = ' '
# SRAR = '*'
# rows = int(input('Введите количество рядов: '))
# spaces = rows - 1
# stars = 1
# for _ in range(rows):
#     print(SPACE * spaces + SRAR * stars)
#     stars += 2
#     spaces -= 1

# Таблица усножения
for  k in [0,4]:
    for i in range (2, 11):
        res = ''
        for j in range(2 + k, 6 + k):
            res += f'{j:^2} x {i:^2} = {i * j:^2}\t'
        print(res)
    print()