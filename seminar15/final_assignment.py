import os
import logging
from collections import namedtuple
import sys

logging.basicConfig(filename='infopath_log.log', level=logging.INFO, filemode='w', encoding='utf-8')
InfoPathLog = namedtuple('InfoPathLog', ['name', 'extension', 'is_directory', 'parent_directory'])

def get_file_info(path):
    try:
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            is_dir = os.path.isdir(full_path)
            infopath_log = InfoPathLog(
                name=os.path.splitext(item)[0] if not is_dir else item,
                extension=os.path.splitext(item)[1] if not is_dir else '',
                is_directory=is_dir,
                parent_directory=os.path.basename(os.path.dirname(path)))        
            logging.info(f"Имя файла/каталога: {infopath_log.name}, Расширение, если это файл: {infopath_log.extension}, Флаг каталога: {infopath_log.is_directory}, Родительский каталог: {infopath_log.parent_directory}")

    except Exception as e:
        logging.error(f'Ошибка! Системе не удалось найти указанный путь: {path}')

if __name__ == '__main__':   
    if len(sys.argv) != 2:
        print("Пример запуска: python final_assignment.py <путь до директории на ПК>")
    else:
        directory_path = sys.argv[1]
        get_file_info(directory_path)