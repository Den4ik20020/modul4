class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError(f"Недопустимый возраст: {age}")
        self.__age = age

    @age.deleter
    def age(self):
        print("Delete Name!")
        self.age = None


person = Person("Серёжа", 16)
print(person.age)
person.age = 20
print(person.age)
del person.age
print(person.age)
