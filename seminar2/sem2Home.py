# Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.
num = 255

def tobase(num: int, base: int):
    hex_map = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
               6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B',
               12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = ""
    while num > 0:
        result = hex_map[num % base] + result
        num //= base
    return result

print('Шестнадцатеричное представление числа:',tobase(num, 16))
print('Проверка результата:',hex(num))

# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем. Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно. Для проверки своего кода используйте модуль fractions.
from fractions import Fraction

frac1 = "1/2"
frac2 = "1/3"

def add_mult(frac1, frac2, operation):
    num1, denom1 = map(int, frac1.split("/"))
    num2, denom2 = map(int, frac2.split("/"))
    if operation == 's':      
        tmp_num = num1 * denom2 + num2 * denom1        
    else:
        tmp_num = num1 * num2
    tmp_denom = denom1 * denom2
    return f"{tmp_num}/{tmp_denom}"

print("Сумма дробей:", add_mult(frac1, frac2, 's'))
print("Произведение дробей:", add_mult(frac1, frac2, 'm'))

print("Сумма дробей:", Fraction(frac1) + Fraction(frac2))
print("Произведение дробей:", Fraction(frac1) * Fraction(frac2))