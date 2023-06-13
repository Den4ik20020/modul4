def my_func(a, b, c, *args):
    print(a, b, c)
    some = args[2]
    print(some)

my_func(10, 20, 30, 40, 50, 60, 70, 'hello')
