def my_func(a, b, **kwargs):
    print(a, b)
    some = kwargs.get('d')

my_func(a=10, b=20, c=30, d=40, f=50)
