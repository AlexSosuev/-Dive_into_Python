# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
# Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка ферзей на шахматной доске, в которой ни один ферзь не бьет другого. Другими словами, ферзи размещены таким образом, что они не находятся на одной вертикали, горизонтали или диагонали.
# Список из 4х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо.

from random import randint
def is_attacking(q1, q2):
    return q1[0] == q2[0] or q1[1] == q2[1] or q1[0] - q2[0] == q1[1] - q2[1]


def check_queens(queens):
    for i in range(len(queens) - 1):
        for j in range(1 + i, len(queens)):
            if is_attacking(queens[i], queens[j]):
                return False
    return True

def generate_boards():
    board_list = []
    while len(board_list) < 4:
        test_set = []
        while len(test_set) < 8:
            if not test_set:
                test_set.append((randint(1, 9), randint(1, 9)))
            x, y = (randint(1, 9), randint(1, 9))
            if not is_attacking(test_set[-1], (x, y)):
                test_set.append((x, y))
        if check_queens(test_set):
            board_list.append(test_set)
    return board_list