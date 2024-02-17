# Задание No5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.
from task_4 import create_pull_of_files


def create_different_files(**kwargs):
    if kwargs:
        for ext, count in kwargs.items():
            create_pull_of_files(ext=ext, quantity=count)


if __name__ == '__main__':
    create_different_files(jpg=4, avi=4, mov=2, tiff=2, txt=2, doc=3)
