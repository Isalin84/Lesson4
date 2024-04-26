from abc import ABC, abstractmethod

# Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        """Метод для атаки, должен быть реализован в производных классах."""
        pass

# Конкретный класс для Меча
class Sword(Weapon):
    def attack(self):
        return "наносит удар мечом"

# Конкретный класс для Лука
class Bow(Weapon):
    def attack(self):
        return "наносит удар из лука"

# Класс бойца, который может использовать различное оружие
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None  # Изначально боец без оружия

    def change_weapon(self, weapon):
        """Метод для смены оружия бойца."""
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.__class__.__name__.lower()}.")

    def attack(self):
        """Метод для атаки, использующий оружие бойца."""
        if self.weapon:
            action = self.weapon.attack()
            print(f"{self.name} {action}.")
        else:
            print(f"{self.name} не может атаковать, так как оружие не выбрано")

# Класс монстра
class Monster:
    def __init__(self, name):
        self.name = name

    def is_defeated(self):
        """Метод, вызываемый, когда монстр побежден."""
        print(f"{self.name} побежден!")

# Функция для демонстрации боя между бойцом и монстром
def fight(fighter, monster):
    if fighter.weapon:
        fighter.attack()
        monster.is_defeated()
    else:
        print("Боец не может атаковать без оружия!")

# Создаем объекты для демонстрации
fighter = Fighter("Боец")
monster = Monster("Монстр")

# Пример использования меча
fighter.change_weapon(Sword())
fight(fighter, monster)

# Пример использования лука
fighter.change_weapon(Bow())
fight(fighter, monster)
