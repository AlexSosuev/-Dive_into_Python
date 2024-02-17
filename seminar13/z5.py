# 📌 Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы: 
# 📌 загрузка данных (функция из задания 4) 
# 📌 вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя в множестве используйте магический метод проверки на равенство пользователей. Если такого пользователя нет, вызывайте исключение доступа. А если пользователь есть, получите его уровень из множества пользователей. 
# 📌 добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.

from my_func import create_user_list
from my_class import User
from my_exception import LevelError, AccessError, UserIDError
import json

class UserSystem:
    def __init__(self, base_path: str):
       self.path = base_path
       self.access = False
       self.user_base = UserSystem._load_user_base(base_path)
       self.authorized_user = None

    @staticmethod
    def _load_user_base(path):
        return create_user_list(path)
    
    def _save_new_user(self, new_user: User):
        self.user_base.add(new_user)
        data = {}
        for user in self.user_base:
            if str(user.level) in data:
                data[str(user.level)][user.u_id] = user.name
            else:
                data[str(user.level)] = {user.u_id, user.name}
        with open(self.path, 'w', encoding='utf-8') as data_file:
            json.dump(data, data_file, indent=4,ensure_ascii=False)
        self.user_base = create_user_list(self.path)

    def login(self, login_user: User):
        for cur_user in self.user_base:
            if cur_user == login_user:                    
                self.authorized_user = cur_user
                self.access = True
                print(f'\nЗдравствуйте, {cur_user.name}! Доступ разрешен!\n')
                return cur_user.level
        raise AccessError('Пользователь стакими данными отсутсвует в базе')

    def new_user(self, name:str, u_id: str, level: int):
        if self.access:
            if int(self.authorized_user.level) < level:
                raise LevelError(f'Уровень нового пользователя должен быть меньше Вашего ({int(self.authorized_user.level)} > {level})')
            id_list = {cur_user.u_id for cur_user in self.user.base}
            if u_id in id_list:
                raise UserIDError(f'Пользователь с ID {u_id} уже существует')
            new_user = User(name, u_id, level)
            self._save_new_user(new_user)
        else:
            raise AccessError('Система не активна')

    def user_list(self):
        return '\n'.join([user.__str__() for user in self.user_base])
    
    def __str__(self):
        return f'Система {"активна" if self.access else "не активна"}' + (f'{self.authorized_user}' if self.authorized_user else '')

if __name__ == '__main__':
    our_system = UserSystem('worker.json')
    user = User('Stoun', '2345')
    print(our_system)
    print(our_system.user_list())
    print()
    user = User('Stoun', '2345')
    print(our_system.login(user))
    print(our_system)
    our_system.new_user('Valera', '12345', 4)