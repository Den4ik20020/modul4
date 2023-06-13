# def recurs(count):
#     print(count)
#     if count == 5:
#         return
#     recurs(count + 1)
#     print(count)
#
#
# recurs(0)

# n = 1
#
# for i in range(1, 6):
#     n *= i
#
# print(n)


def factorial(number):
    if number == 1:
        return number
    return number * factorial(number - 1)


print(factorial(256))

