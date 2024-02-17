# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида 10.25%.
# В результате result получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.
# Не забудьте распечатать в конце результат.

salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]

print(result := {name: rate * float(prem.strip('%')) / 100 for name, rate, prem in zip(names, salary, bonus)})