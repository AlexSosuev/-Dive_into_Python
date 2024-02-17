# Создайте класс Архив, который хранит пару свойств. Например, число и строку. При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списковархивов list-архивы также являются свойствами экземпляра

class Archive:
    num_str_list = []

    def __new__(cls, str_arg, num_arg):
        instance = super().__new__(cls)
        instance.str_arg = str_arg
        instance.num_arg = num_arg
        instance.num_str_list = cls.num_str_list.copy()
        cls.num_str_list.append(instance)
        return instance
    
    def __str__(self):
        return f'Объект Архив ({self.str_arg} {self.num_arg}) Архив {self.num_str_list}'
    
    def __repr__(self):
        return f'{self.str_arg} {self.num_arg}'

a = Archive(1, 'A')
b = Archive(2, 'B')
c = Archive(3, 'C')
d = Archive(4, 'D')

print(a)
print(a.num_str_list)
print(b)
print(b.num_str_list)
print(c)
print(c.num_str_list)
print(d)
print(d.num_str_list)