import home_1 
import inspect

functions_list = inspect.getmembers(home_1)

with open('__init__.py', 'a', encoding='utf-8') as f:
    for func, attribute in functions_list:
        if inspect.isfunction(attribute):
            f.write(func + '\n')