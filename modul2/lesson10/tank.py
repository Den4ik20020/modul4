import abc


class AbstactTank(abc.ABC):
    def __init__(self, armor, damage, speed, health):
        self.armor = armor
        self.damage = damage
        self.speed = speed
        self.health = health

    def shoot(self, enemy):
        pass

    def health_down(self, damage):
        pass


class Mouse(AbstactTank):
    def __str__(self):
        return "Mouse"

    def shoot(self, enemy):
        print(f"MOUSE: Стреляю по врагу {enemy}")
        enemy.health_down(self.damage)

    def health_down(self, damage):
        total_damage = damage / self.armor
        print(f"MOUSE: В меня попали {total_damage}")
        self.health -= total_damage


class T34(AbstactTank):
    def __str__(self):
        return "T34"

    def shoot(self, enemy):
        print(f"T34: Стреляю по врагу {enemy}")
        enemy.health_down(self.damage)

    def health_down(self, damage):
        total_damage = damage / self.armor
        print(f"T34: В меня попали {total_damage}")
        self.health -= total_damage


class SuperT34(T34):
    def __init__(self, armor, damage, speed, health, boost):
        super().__init__(armor * boost, damage, speed, health)

    def __str__(self):
        return "SuperT34"

    def shoot(self, enemy):
        print(f"SuperT34: Стреляю по врагу {enemy}")
        enemy.health_down(self.damage)

    def health_down(self, damage):
        total_damage = damage / self.armor
        print(f"SuperT34: В меня попали {total_damage}")
        self.health -= total_damage


mouse = Mouse(3000, 100, 50, 10)
t34 = T34(1100, 120, 60, 10)

mouse.shoot(t34)
t34.shoot(mouse)

super_T34 = SuperT34(1000, 10000000, 1000000, 1, 10)
mouse.shoot(super_T34)
