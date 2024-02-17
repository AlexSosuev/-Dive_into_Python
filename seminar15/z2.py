# На семинаре про декораторы был создан логирующий декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# Напишите аналогичный декоратор, но внутри используйте модуль logging.
import logging
from functools import wraps

LOG_FORMAT = '%(asctime)s - %(message)s'
logging.basicConfig(filename='decorator_logs.log', level=logging.DEBUG, format=LOG_FORMAT, encoding='utf-8')

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f'Функция{func.__name__}, которая вызывает аргументы {args}'
                     f' ключевые аргументы {kwargs}')
        result = func(*args, **kwargs)
        logging.info(f'Функция: {func.__name__} возвращает результат выполнения {result}')
        return result
    return wrapper

@log_decorator
def add(x, y):
    return x + y

print(add(4,y=5))