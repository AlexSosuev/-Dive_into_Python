# Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
# Вынесите общие свойства и методы классов в класс Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.


class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def info(self):
        print(self.name, self.age)

class Fish(Animal):
    def __init__(self, name, age, depth):
        super().__init__(name, age)
        self.depth = depth

    def type_fish(self):
        if 0 < self.depth < 4:
            print('мелководная')
        elif 4 <= self.depth < 8:
            print('средневодная')
        else:
            print('глубоководная')

    def info(self):
        print('Это рыбы')

class Bird(Animal):
    def __init__(self, name, age, wingspan):
       super().__init__(name, age)
       self.wingspan = wingspan

    def len_wing(self):
        return self.wingspan / 2

class Mammal(Animal):
    def __init__(self, name, age, weight):
       super().__init__(name, age)
       self.weight = weight

    def info(self):
        print('Это млекопитающеи')

    def category(self):
        if 1 < self.weight < 10:
            print('мелкие')
        elif 10 <= self.weight < 50:
            print('средние')
        else:
            print('крупные')


if __name__ == '__main__':
    fish = Fish('Акула', 2 , 7)
    fish.info()
    fish.type_fish()

    bird = Bird('Соловей', 1, 10)
    bird.info()
    print(bird.len_wing())

    elephant = Mammal('Слон', 8, 90)
    elephant.info()
    elephant.category()