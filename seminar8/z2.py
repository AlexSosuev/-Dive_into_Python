# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).  После каждого ввода 
# добавляйте новую информацию в JSON файл. Пользователи группируются по уровню доступа. Идентификатор пользователя выступает ключём для имени. 
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа. При перезапуске функции уже записанные в файл данные должны сохраняться.

import json

def input_user_data():
    user_data = {}
    while True:
        name = input("Введите имя (или 'exit' для выхода): ")
        if name.lower() == 'exit':
            break
        id_number = input("Введите личный идентификатор: ")
        while True:
            access_level_str = input("введите уровень доступа (от 1 до 7): ")
            if access_level_str.isdigit():
                access_level = int(access_level_str)
                if 1 <= access_level <= 7:
                    break
            print("Некорректный уровень доступа. Пожалуйста, введите число от 1 до 7.")
        user_data[id_number] = {
            'name' : name,
            'access_level' : access_level
        }
        save_user_data(user_data, access_level)


def save_user_data(user_data, access_level):
    filename = f'users_access_level_{access_level}.json'
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    data.update(user_data)
    with open(filename, w, encoding = 'utf-8') as file:
        json.dump(data, file, indent = 4)

if __name__ == "__main__":
    input_user_data