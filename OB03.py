import pickle

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} makes a sound.")

    def eat(self):
        print(f"{self.name} is eating.")

class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} tweets.")

class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} roars.")

class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} hisses.")

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Added {animal.name} to the zoo.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Added {staff_member.name} to the staff.")

class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} feeds {animal.name}.")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} is treating {animal.name}.")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

def save_zoo(zoo, filename='zoo.pkl'):
    with open(filename, 'wb') as f:
        pickle.dump(zoo, f)
    print("Zoo saved to file.")

def load_zoo(filename='zoo.pkl'):
    try:
        with open(filename, 'rb') as f:
            zoo = pickle.load(f)
        print("Zoo loaded from file.")
        return zoo
    except FileNotFoundError:
        print("File not found. Creating a new zoo.")
        return Zoo()

# Создание объектов животных
parrot = Bird("Polly", 5)
tiger = Mammal("Tony", 4)
snake = Reptile("Sly", 2)

# Создание зоопарка и добавление животных и сотрудников
zoo = Zoo()
zoo.add_animal(parrot)
zoo.add_animal(tiger)
zoo.add_animal(snake)

keeper = ZooKeeper("Joe")
vet = Veterinarian("Emma")

zoo.add_staff(keeper)
zoo.add_staff(vet)

# Демонстрация полиморфизма
animal_sound(zoo.animals)

# Действия сотрудников
keeper.feed_animal(parrot)
vet.heal_animal(snake)

# Сохранение и загрузка зоопарка
save_zoo(zoo)
zoo_loaded = load_zoo()
