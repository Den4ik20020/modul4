import abc


class User(abc.ABC):
    def __init__(self, health, damage, method_of_attack):
        self.health = health
        self.damage = damage
        self.method_of_attack = method_of_attack

    def attack(self, enemy):
        pass

    def health_down(self, damage):
        pass


class Magician(User):
    method_of_attack = 'magic'

    def __str__(self):
        return "magician"

    def attack(self, enemy):
        print(f"Маг: Атакую {enemy} ")
        enemy.health_down(self.damаge)

    def health_down(self, damage):
        print(f"Маг: Меня ранили {damage}")
        self.health -= damage


class Warrior(User):
    method_of_attack = 'sword'

    def __str__(self):
        return "Warrior"

    def attack(self, enemy):
        print(f"Воин: Атакую {enemy} ")
        enemy.health_down(self.damаge)

    def health_down(self, damage):
        print(f"Воин: Меня ранили {damage}")
        self.health -= damage//10


class Archer(User):
    method_of_attack = 'bow'

    def __str__(self):
        return "Archer"

    def attack(self, enemy):
        print(f"Лучник: Атакую {enemy} ")
        enemy.health_down(self.damаge)

    def health_down(self, damage):
        print(f"Лучник: Меня ранили {damage}")
        self.health -= damage