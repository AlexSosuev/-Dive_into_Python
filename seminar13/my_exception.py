# 📌 Создайте класс с базовым исключением и дочерние классыисключения: ○ ошибка уровня, ○ ошибка доступа.

class MyError(Exception):
    def __init__(self, msg, message):
        self.message = message
        self.msg = msg

    def __str__(self):
        return f'{self.msg}: {self.message}'


class LevelError(MyError):
    def __init__(self, message):
        super().__init__('Ошибка уровня', message)


class AccessError(MyError):
    def __init__(self, message):
        super().__init__('Ошибка доступа', message)

class UserIDError(MyError):
    def __init__(self, message):
        super().__init__('Ошибка создания пользователя', message)

if __name__ == '__main__':
    raise AccessError('не хватает прав')