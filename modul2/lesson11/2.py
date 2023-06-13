#Singletone
class A:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, a, b):
        self.a = a
        self.b = b


a1 = A(10, 20)
a2 = A(30, 40)
a3 = A(50, 60)

print(a1.a,  a1.b)
print(a2.a,  a2.b)
print(a3.a,  a3.b)

print(a1 is a2 is a3)
