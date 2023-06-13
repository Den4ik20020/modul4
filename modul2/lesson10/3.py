class A:
    def c(self):
        pass


class B(A):
    pass


print(dir(B))
