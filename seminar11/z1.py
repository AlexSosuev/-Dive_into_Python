# Создайте класс Моя Строка, где: будут доступны все возможности str, дополнительно хранятся имя автора строки и время создания (time.time)
import time
class MyString(str):
    def __new__(cls, value, autor):
        return super(MyString, cls).__new__(cls, value)
    
    def __init__(self, value, autor):        
        self.autor = autor
        self.creation_time = time.time()

autor = 'Pushkin'
my_string = MyString('Произведение', autor)
print(my_string)
print(my_string.autor)
print(my_string.creation_time)