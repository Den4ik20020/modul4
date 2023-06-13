def my_func(*args, **kwargs):
    print(args)
    print(kwargs)

my_func(10, 20, 30, b=40, c=50, d=60)
