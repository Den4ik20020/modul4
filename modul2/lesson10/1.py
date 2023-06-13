class Animal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def breath(self):
        print("Это животное дышит")


class Cat(Animal):
    pass


cat_1 = Cat("Паштет", 15)
cat_1.breath()
print(cat_1.weight, cat_1.name)
