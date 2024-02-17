# Создайте декоратор с параметром. Параметр - целое число, количество запусков декорируемой функции.
from functools import wraps

def deco_with_params(count: int):
    result = []
    def outer(func):
        @wraps(func)
        def inner(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)
        return inner
    return outer
if __name__ == '__main__':
    @deco_with_params(5)
    def simple_func(message: str):
        print(message)

    simple_func('hi')