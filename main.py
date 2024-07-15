
# Конечно, давайте начнем с создания базового класса Animal:

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

# Теперь создадим подклассы Bird, Mammal и Reptile, наследующие от Animal:

class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        return "Chirp chirp"

    def fly(self):
        return f"{self.name} is flying"

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return "Growl"

    def run(self):
        return f"{self.name} is running"

class Reptile(Animal):
    def __init__(self, name, age, scale_pattern):
        super().__init__(name, age)
        self.scale_pattern = scale_pattern

    def make_sound(self):
        return "Hiss"

    def bask(self):
        return f"{self.name} is basking in the sun"

# Далее, реализуем функцию animal_sound() для демонстрации полиморфизма:

def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

# Пример использования
bird1 = Bird("Sparrow", 2, 10)
mammal1 = Mammal("Tiger", 5, "orange")
reptile1 = Reptile("Snake", 3, "diamond")

animal_sound([bird1, mammal1, reptile1])

# Теперь создадим класс Zoo с использованием композиции:

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff):
        self.staff.append(staff)

# Пример использования
zoo = Zoo()
zoo.add_animal(bird1)

# Наконец, создадим классы для сотрудников:

class ZooKeeper:
    def feed_animal(self, animal):
        return f"Feeding {animal.name}"

class Veterinarian:
    def heal_animal(self, animal):
        return f"Healing {animal.name}"

# Пример использования
zookeeper = ZooKeeper()
veterinarian = Veterinarian()
print(zookeeper.feed_animal(bird1))
print(veterinarian.heal_animal(mammal1))

# Для дополнительных функций, таких как сохранение информации о зоопарке в файл и загрузку, можно использовать модуль pickle или json для сериализации объектов. Например, чтобы сохранить состояние зоопарка:

import pickle

# Сохранение состояния зоопарка
with open('zoo_state.pkl', 'wb') as file:
    pickle.dump(zoo, file)

# И для загрузки:

# Загрузка сохраненного состояния зоопарка
with open('zoo_state.pkl', 'rb') as file:
    saved_zoo = pickle.load(file)

print(saved_zoo.animals)

# Это базовый пример реализации задачи.
# Конечно, можно добавить дополнительные функции и улучшения по мере необходимости.