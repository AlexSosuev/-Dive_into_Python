# Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:

# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# f. Папка test_folder доступна из текущей директории

import os

def rename_files(old_name_diapason: list = None, desired_name: str = 'new_file', num_digits: int = 3,
                 source_ext: str = 'txt', target_ext: str = 'new'):
    count = 0
    folder_path = 'test_folder'
    
    for file in os.listdir(folder_path):
        name, extension = os.path.splitext(file)        
        if extension[1:] == source_ext:
            count += 1
            out_name = ''            
            if old_name_diapason:
                out_name += name[old_name_diapason[0] - 1:old_name_diapason[1]]            
            out_name += f'{desired_name}{count:0{num_digits}}' + '.' + target_ext
            os.rename(os.path.join(folder_path, file), os.path.join(folder_path, out_name))

#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")

# import os
# def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=None):
#     new_names = []
#     files = os.listdir('test_folder')
#     filtered_files = [file for file in files if file.endswith(source_ext)]
#     filtered_files.sort()
#     num = 1
#     for file in filtered_files:
#         name = os.path.splitext(file)[0]
#         if name_range:
#             name = name[name_range[0]-1:name_range[1]]
#         new_name = desired_name + str(num).zfill(num_digits) + '.' + target_ext
#         path_old = os.path.join(os.getcwd(), folder_name, file)
#         path_new = os.path.join(os.getcwd(), folder_name, new_name)
#         os.rename(path_old, path_new)
#         num += 1