# Задание No7
# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
import os
import shutil

dict_for_sort = {'video': ['avi', 'mov'], 'pictures': ['jpg', 'tiff'], 'text': ['txt', 'doc']}


def sort_my_folder(folder: str = 'sample', **kwargs):
    if not os.path.exists(folder):
        print('wrong folder')
        exit(1)
    for file in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, file)):
            for sub_folder, extensions in kwargs.items():
                if file.split('.')[-1] in extensions:
                    if not os.path.exists(sub_folder):
                        os.makedirs(sub_folder)
                    shutil.move(os.path.join(folder, file), os.path.join(sub_folder, file))


if __name__ == '__main__':
    sort_my_folder(**dict_for_sort)
